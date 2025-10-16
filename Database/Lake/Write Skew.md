---
aliases:
  - Phantoms
  - Write Skews
---
**Write Skew** - is a generalization of [[Lost Update]] problem.
While **[[Lost Update]]** *happens to the* **same record**,
	**[[Write Skew]]** *happens to* **separate records**. 

[[Transaction]] **reads something** (premise), 
**makes decision** based on it 
and **performs write**, 
which leads to **oudated premise** of another [[Transaction]]. 

Only **[[Snapshot Isolation]]** prevents it.

> **Example:**  Meeting room booking (See [[Examples of Write Skew#^booking]]).

This is the anomaly when two **parallel [[Transaction|Transactions]] run read queries**, on which results depends further **update logic**, which results in **logic executed in both cases** instead of one.

**Write skew** can happen **if write depends on presence/absence of some records**, while this **write may insert new or modify this set of records** on it's own. Hence, if two transactions read the value, first makes the modification, then second is not aware that subset has changed and write skew happens.

## Phantoms causing write skew

**Phantom** - the effect when **write in one [[Transaction]] changes the query result in another** after this query was executed.

Basically phantoms are ***revealed** when* we ***read*** the set of records from the database ***twice***. When we see a different set from the one we've seen it before, - that's a phantom.

**Pattern of [[Write Skew]]** is following:
1. **query** searches for rows that ***match*** some **condition**;
2. depending on the result of query, **app decides what to do** (either report an error or make the write);
3. if condition from step 2 is satisfied, app **makes a write and commits** the [[Transaction]]. 
   The committed **write *affects the* result *of the* query** from step 1.

## Solutions

Solutions to [[Write Skew]]:
- **Automatic** - using **[[Serializable]]**;
- **DB constraints** to enforce [[Consistency]] (e.g. [[PostgreSQL Exclude Constraint]]);
- **[[Explicit locking]]** on the rows that [[Transaction]] depend on;
- **[[Materializing conflicts]]** - last resort if transaction depends on absence of rows and is not related to any entity that could be locked (or not possible to be locked under circumstances).
