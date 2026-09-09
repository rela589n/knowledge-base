---
aliases:
  - Timestamp-based Synchronization
---
> **TLDR**: it has more problems than I thought:
> 
> - [[Clock Drift]]
> - Commit racing with an in-flight Sync
> - Uniqueness of `updatedAt`
> 
> Check the [doc](https://docs.google.com/document/d/1lIldIy_6iP2wKJVtxMsa7m2aUTTq1HHwxNo7wnMYt8Q/edit?tab=t.0)

We must filter by two values:

```sql
SELECT * FROM entities e
WHERE (e.updated_at, e.id) > (:lastUpdatedAt, :lastId)
  AND a.updated_at <= now() - interval '30 seconds'
ORDER BY e.updated_at, e.id
LIMIT :limit
```
And to solve [[Clock Drift]], we might subtract `interval 30 sec` 

## Why the cursor holds two values  
  
### The context  
  
A partner reads the entities in pages. The server sends 100 entities in each page.  
  
The cursor is the marker at the end of a page. The partner sends the cursor back. The server then continues from the marker.  
  
The cursor must do two things:  
- It must not skip an entity.  
- It must not send the same page again and again.  
  
The server sorts the entities by the time of the last change. So you can put that time in the cursor. This is not sufficient. The example below shows why.  
  
### The example data  
  
Five entities are in the database. An operator made one bulk edit at 10:05. The edit set the same time on three entities.  
  
| `updated_at` | `id` | Name |  
|---|---|---|  
| 10:00 | A | Alpha |  
| 10:05 | B | Bravo |  
| 10:05 | C | Charlie |  
| 10:05 | D | Delta |  
| 10:09 | E | Echo |  
  
The page size is 2. This keeps the example short. The behavior is the same at 100.  
  
### Try 1 — the cursor holds only the time. The server uses `>`  
  
| Page | Query | Result | New cursor |  
|---|---|---|---|  
| 1 | `updated_at > 00:00` | Alpha, Bravo | `10:05` |  
| 2 | `updated_at > 10:05` | Echo | `10:09` |  
| 3 | `updated_at > 10:09` | *empty* | — |  
  
Charlie and Delta have the time 10:05. The time 10:05 is not more than 10:05. Therefore the query does not find them.  
  
**The server lost two entities. The partner never gets them.**  
  
### Try 2 — the cursor holds only the time. The server uses `>=`  
  
| Page | Query | Result | New cursor |  
|---|---|---|---|  
| 1 | `updated_at >= 00:00` | Alpha, Bravo | `10:05` |  
| 2 | `updated_at >= 10:05` | Bravo, Charlie | `10:05` |  
| 3 | `updated_at >= 10:05` | Bravo, Charlie | `10:05` |  
  
The cursor does not change. The server sends the same two entities again and again.  
  
**The partner is in a loop. Delta and Echo never come.**  
  
### Try 3 — the cursor holds the time and the id  
  
The server compares the pair `(updated_at, id)`.  
  
| Page | Query | Result | New cursor |  
|---|---|---|---|  
| 1 | `(updated_at, id) > (00:00, "")` | Alpha, Bravo | `(10:05, B)` |  
| 2 | `(updated_at, id) > (10:05, B)` | Charlie, Delta | `(10:05, D)` |  
| 3 | `(updated_at, id) > (10:05, D)` | Echo | `(10:09, E)` |  
| 4 | `(updated_at, id) > (10:09, E)` | *empty* | — |  
  
**The partner gets all five entities. The partner gets each entity one time.**  
  
### How the pair comparison works  
  
Postgres compares a pair in two steps:  
1. It compares the first value.  
2. If the first values are equal, it compares the second value.  
  
These are the three comparisons from page 2 of Try 3:  
  
| Comparison | Step 1: the times | Step 2: the ids | Result |  
|---|---|---|---|  
| `(10:05, B) > (10:05, B)` | equal | `B > B` is false | **false** — Bravo does not come again |  
| `(10:05, C) > (10:05, B)` | equal | `C > B` is true | **true** — Charlie comes |  
| `(10:09, E) > (10:05, D)` | `10:09 > 10:05` is true | not used | **true** — Echo comes |  
  
The id has an effect only when the times are equal. In all other rows the time decides.  
  
### The rule  
  
The sort key must be unique. If two entities have the same sort key, then the words *"the entities after this entity"* have more than one answer. The server cannot make a correct page.  
  
The time alone is not unique. The time and the id together are unique. Therefore the cursor holds both.  
  
Postgres supports this comparison directly. The `ORDER BY` must use the same two columns in the same sequence:  
  
```sql  
WHERE (a.updated_at, a.id) > (:lastUpdatedAt, :lastId)
ORDER BY a.updated_at, a.id
LIMIT :limit
```  
  
The index `(updated_at, id)` from makes this query fast.  
The index sequence must be the same as the `ORDER BY` sequence.