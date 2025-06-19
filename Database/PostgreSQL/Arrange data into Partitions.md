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

To get the first and last ids of each partition, use

```sql
SELECT DISTINCT partition,
                first_value(id) over p,
                last_value(id) over p
FROM (SELECT id,
             ntile(2048) OVER (ORDER BY id) partition
      FROM users) parts
WINDOW p AS (PARTITION BY partition)
ORDER BY partition;
```

It uses [[WINDOW clause]]