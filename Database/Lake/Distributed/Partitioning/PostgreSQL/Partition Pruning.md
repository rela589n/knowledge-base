[Doc](https://www.postgresql.org/docs/current/ddl-partitioning.html#DDL-PARTITION-PRUNING)

Planner examines each [[Partition]] and proves if it could contain records, requested by the query. If not, it's excluded from the search.

```sql
SELECT count(*) FROM measurement WHERE logdate >= DATE '2008-01-01';
```
