[[PostgreSQL]]

~~It seems to be possible to run multiple queries over the same connection at the same time.~~

One may try to run these two over the same connection and see the result:

```sql
SELECT 1 as result, pg_sleep(5);  
SELECT 2 as result, pg_sleep(5);
```

> It is not documented, and should not be used. It fails if run in transaction.
