---
aliases:
  - Inverted Index
---
**Generalized Inverted Index**

```sql
CREATE INDEX users_serch_vector_idx ON users USING GIN (search_vector)
```

GIN index can be used for:
- [[PostgreSQL TSVector|search data types]];
- [[Array|arrays]];
- [[PostgreSQL Json|json objects]].

GIN Index is a [[B-Tree|B-Tree Index]] built over every indexable key from the original documents.
It stores set of `(key, posting list)` pairs that cover full range of indexed items.

**Indexed *Item*** - document to be indexed (e.g. compound value), contains key / keys.

**Indexed *Key*** - element of the indexed item. GIN index includes keys rather than items.

**Postings List** - set of indexed item row ids (heap pointers), in which the indexed key occurs.

[Diagram](https://lucid.app/lucidchart/ea3581ae-f914-401b-8703-80c85b9dc602/edit?beaconFlowId=0A761ADB03FDAB53&invitationId=inv_204d3093-3d94-4792-9096-6767df47148c&page=0_0#)
![[GIN Key BTree.png]]

![[GIN index example.png]]

Resources:
- https://www.postgresql.org/docs/current/gin.html
- https://habr.com/ru/companies/postgrespro/articles/340978/
