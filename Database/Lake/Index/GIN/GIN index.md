Generalized Inverted Index

```sql
CREATE INDEX users_serch_vector_idx ON users USING GIN (search_vector)
```

GIN index could be used for:
- [[PostgreSQL TSVector|search data types]];
- [[PostgreSQL Array|arrays]];
- [[PostgreSQL Json|json objects]].

GIN Index is [[BTree]] built of every indexable key from the original document. It stores set of `(key, posting list)` pairs that cover full range of indexed items.

**Indexed *Item*** - the complete document (e.g. composite value) that has key / keys to be indexed.

**Indexed *Key*** - element of the indexed item. GIN index included keys rather than items.

**Posting List** - set of indexed item row ids (heap pointers), in which indexed key occurs.

[Diagram](https://lucid.app/lucidchart/ea3581ae-f914-401b-8703-80c85b9dc602/edit?beaconFlowId=0A761ADB03FDAB53&invitationId=inv_204d3093-3d94-4792-9096-6767df47148c&page=0_0#)
![[GIN Key BTree.png]]

![[GIN index example.png]]

Resources:
- https://www.postgresql.org/docs/current/gin.html
- https://habr.com/ru/companies/postgrespro/articles/340978/
