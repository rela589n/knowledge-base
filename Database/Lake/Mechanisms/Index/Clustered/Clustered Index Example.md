Generate users:

```sql
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

INSERT INTO users (id, created_at, updated_at, email, password_hash, secret_key)
SELECT uuid_generate_v4()                                  as id,
       NOW() - (random() * INTERVAL '365 days')            as created_at,
       NOW() - (random() * INTERVAL '30 days')             as updated_at,
       'user' || generate_series || '@example.com'         as email,
       '$2y$10$' || encode(gen_random_bytes(22), 'base64') as password_hash,
       encode(gen_random_bytes(32), 'hex')                 as secret_key
FROM generate_series(1, 10000);
```

Generate events:

```sql
INSERT INTO user_events (id, user_id, timestamp, type)  
SELECT uuid_generate_v4()                             as id,  
       user_ids.ids[ceil(random() * user_ids.length)] as user_id,  
       now() - (random() * INTERVAL '90 days')        as timestamp,  
       types.values[ceil(random() * 10)]              as type  
FROM (SELECT array_agg(id) as ids, count(id) as length FROM users) user_ids,  
     (SELECT ARRAY ['login', 'logout', 'view_page', 'click_button', 'form_submit', 'file_upload', 'search', 'purchase', 'profile_update', 'password_change'] values) as types,  
     generate_series(1, 20000000) as gen  
;
```

> Note that it's around 2000 events per each user.
> Also note that order of events is random (they're not sorted by user id after insert).

Run [[PostgreSQL VACUUM|VACUUM]]

```sql
VACUUM ANALYSE;
```

Samples:

```sql
SELECT id, user_id FROM user_events TABLESAMPLE system(1) LIMIT 10;
```

Select Query:

```postgresql
EXPLAIN ANALYZE  
SELECT *  
FROM user_events  
WHERE user_id = 'db0bd4b0-71db-462d-852d-f50300806e1f';
```

BEFORE CLUSTER:
```
Bitmap Heap Scan on user_events  (cost=27.93..7418.48 rows=1999 width=50) (actual time=2.938..10.707 rows=2042 loops=1)
  Recheck Cond: (user_id = '78087ef6-f4fe-4e2c-879b-8f64197afaf5'::uuid)
  Heap Blocks: exact=2029
  ->  Bitmap Index Scan on idx_36d54c77a76ed395  (cost=0.00..27.43 rows=1999 width=0) (actual time=2.596..2.596 rows=2042 loops=1)
        Index Cond: (user_id = '78087ef6-f4fe-4e2c-879b-8f64197afaf5'::uuid)
Planning Time: 0.054 ms
Execution Time: 10.896 ms
```

Cluster by user id:

```postgresql
CLUSTER user_events USING idx_36d54c77a76ed395;
VACUUM ANALYSE;
```

The same query, being CLUSTERED:

```
Index Scan using idx_36d54c77a76ed395 on user_events  (cost=0.44..71.01 rows=2147 width=50) (actual time=0.060..0.561 rows=1929 loops=1)
  Index Cond: (user_id = 'db0bd4b0-71db-462d-852d-f50300806e1f'::uuid)
Planning Time: 0.086 ms
Execution Time: 0.756 ms
```

This is with the fact that each user has `~2000` events.
Random [[Table Heap|Heap File]] access is much slower than sequential, as it is with index.
Yet, beware that [[Clustered Index|Clusterization]] of the table is blocking.

