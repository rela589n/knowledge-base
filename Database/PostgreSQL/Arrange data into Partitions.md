---
aliases:
  - PostgreSQL Partition data by key
  - Divide data set into equal parts
---
This will build partition map for user ids into to 2048 parts:

```sql
SELECT id,
       ntile(2048) OVER (ORDER BY id) part
FROM users
```

It uses [[Window function]] over the whole window, ordered by id.
It might've been not ordered, but ordering it creates a consistent range of values, not just random one.

To get the first and last ids of each partition, use query:

```sql
SELECT DISTINCT partition,
                first_value(id) OVER p AS start_id,
                last_value(id) OVER p AS end_id
FROM (SELECT id,
             ntile(2048) OVER (ORDER BY id) partition
      FROM users) parts
WINDOW p AS (PARTITION BY partition)
ORDER BY partition;
```

^fae1e5

It uses [[WINDOW clause]]

If you need to make sure that next partition starts from the first, use this query:

```sql
SELECT DISTINCT ON (partition) partition,
       lag(id, 1) OVER () AS start_id,
       last_value(id) OVER p  AS end_id
FROM (SELECT id,
             ntile(2048) OVER (ORDER BY id) partition
      FROM users) parts
WINDOW p AS (PARTITION BY partition)
ORDER BY partition;
```

> `lag(id, 1) OVER () AS start_id,`

This part operates on the whole window of the result set, always producing the id from the last row.

> last_value(id) OVER p  AS end_id

It operates on the actual users partition, and gets the last id of this partition.

