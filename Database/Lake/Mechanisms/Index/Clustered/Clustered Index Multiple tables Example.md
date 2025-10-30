Create data:

```postgresql
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


INSERT INTO user_events (id, user_id, timestamp, type)
SELECT uuid_generate_v4()                             as id,
       user_ids.ids[ceil(random() * user_ids.length)] as user_id,
       now() - (random() * INTERVAL '90 days')        as timestamp,
       types.values[ceil(random() * 10)]              as type
FROM (SELECT array_agg(id) as ids, count(id) as length FROM users) user_ids,
     (SELECT ARRAY ['login', 'register', 'password_reset_requested', 'password_reset', 'form_submit', 'file_upload', 'search', 'purchase', 'profile_update', 'password_change'] values) as types,
     generate_series(1, 20000000) as gen
;

INSERT INTO user_logged_in_events (id)
SELECT ue.id
FROM user_events ue
WHERE ue.type = 'login';

INSERT INTO user_registered_events (id, email, password_hash)
SELECT ue.id,
       u.email,
       u.password_hash
FROM user_events ue
         JOIN users u ON ue.user_id = u.id
WHERE ue.type = 'register';

ALTER TABLE user_password_reset_request_created_event
    DROP CONSTRAINT FK_EEADDE2CFE7CBBE7;
INSERT INTO user_password_reset_request_created_event (id, password_reset_request_id)
SELECT ue.id,
       uuid_generate_v4()
FROM user_events ue
WHERE ue.type = 'password_reset_requested';

ALTER TABLE user_reset_password_events
    DROP CONSTRAINT FK_BEA9ACFE7CBBE7;
INSERT INTO user_reset_password_events (id, password_reset_request_id)
SELECT ue.id,
       uuid_generate_v4()
FROM user_events ue
WHERE ue.type = 'password_reset';

VACUUM ANALYSE;
```

Query that runs:

```sql
EXPLAIN ANALYZE
SELECT *
FROM user_events
         LEFT JOIN user_logged_in_events ON user_events.id = user_logged_in_events.id
         LEFT JOIN user_registered_events ON user_events.id = user_registered_events.id
         LEFT JOIN user_reset_password_events ON user_events.id = user_reset_password_events.id
         LEFT JOIN user_password_reset_request_created_event
                   ON user_events.id = user_password_reset_request_created_event.id
WHERE user_id = 'd97abd46-8393-45fc-a8bc-0cb1547d50c2';
```

Before CLUSTER:

```
Gather  (cost=1029.59..40998.58 rows=1992 width=208) (actual time=3.461..72.536 rows=2023 loops=1)
  Workers Planned: 1
  Workers Launched: 1
  ->  Nested Loop Left Join  (cost=29.59..39799.38 rows=1172 width=208) (actual time=1.529..48.065 rows=1012 loops=2)
        ->  Nested Loop Left Join  (cost=29.16..30626.69 rows=1172 width=176) (actual time=1.508..38.452 rows=1012 loops=2)
              ->  Nested Loop Left Join  (cost=28.73..21461.06 rows=1172 width=144) (actual time=1.488..29.280 rows=1012 loops=2)
                    ->  Nested Loop Left Join  (cost=28.30..12163.64 rows=1172 width=68) (actual time=1.465..19.791 rows=1012 loops=2)
                          ->  Parallel Bitmap Heap Scan on user_events  (cost=27.88..7391.84 rows=1172 width=52) (actual time=1.432..10.351 rows=1012 loops=2)
                                Recheck Cond: (user_id = '05df16f5-e021-4f13-81cd-e7c1871b1714'::uuid)
                                Heap Blocks: exact=1517
                                ->  Bitmap Index Scan on idx_36d54c77a76ed395  (cost=0.00..27.38 rows=1992 width=0) (actual time=2.386..2.387 rows=2023 loops=1)
                                      Index Cond: (user_id = '05df16f5-e021-4f13-81cd-e7c1871b1714'::uuid)
                          ->  Index Only Scan using user_logged_in_events_pkey on user_logged_in_events  (cost=0.43..4.07 rows=1 width=16) (actual time=0.009..0.009 rows=0 loops=2023)
                                Index Cond: (id = user_events.id)
                                Heap Fetches: 0
                    ->  Index Scan using user_registered_events_pkey on user_registered_events  (cost=0.43..7.93 rows=1 width=76) (actual time=0.009..0.009 rows=0 loops=2023)
                          Index Cond: (id = user_events.id)
              ->  Index Scan using user_reset_password_events_pkey on user_reset_password_events  (cost=0.43..7.82 rows=1 width=32) (actual time=0.008..0.008 rows=0 loops=2023)
                    Index Cond: (id = user_events.id)
        ->  Index Scan using user_password_reset_request_created_event_pkey on user_password_reset_request_created_event  (cost=0.43..7.83 rows=1 width=32) (actual time=0.009..0.009 rows=0 loops=2023)
              Index Cond: (id = user_events.id)
Planning Time: 1.398 ms
Execution Time: 72.840 ms
```

After CLUSTER (Only main table):

```
-- Gather  (cost=1026.56..43344.15 rows=2118 width=208) (actual time=0.968..46.091 rows=2025 loops=1)

--   Workers Planned: 1

--   Workers Launched: 1

--   ->  Nested Loop Left Join  (cost=26.56..42132.35 rows=1246 width=208) (actual time=0.429..28.661 rows=1012 loops=2)

--         ->  Nested Loop Left Join  (cost=26.13..32426.42 rows=1246 width=176) (actual time=0.410..21.693 rows=1012 loops=2)

--               ->  Nested Loop Left Join  (cost=25.71..22725.21 rows=1246 width=144) (actual time=0.394..15.521 rows=1012 loops=2)

--                     ->  Nested Loop Left Join  (cost=25.28..12878.10 rows=1246 width=68) (actual time=0.374..7.440 rows=1012 loops=2)

--                           ->  Parallel Bitmap Heap Scan on user_events  (cost=24.85..7833.79 rows=1246 width=52) (actual time=0.346..0.552 rows=1012 loops=2)

--                                 Recheck Cond: (user_id = '0f39140a-8e99-427e-99ff-a36874fa87cd'::uuid)

--                                 Heap Blocks: exact=17

--                                 ->  Bitmap Index Scan on idx_36d54c77a76ed395  (cost=0.00..24.32 rows=2118 width=0) (actual time=0.609..0.609 rows=2025 loops=1)

--                                       Index Cond: (user_id = '0f39140a-8e99-427e-99ff-a36874fa87cd'::uuid)

--                           ->  Index Only Scan using user_logged_in_events_pkey on user_logged_in_events  (cost=0.43..4.05 rows=1 width=16) (actual time=0.006..0.006 rows=0 loops=2025)

--                                 Index Cond: (id = user_events.id)

--                                 Heap Fetches: 0

--                     ->  Index Scan using user_registered_events_pkey on user_registered_events  (cost=0.43..7.90 rows=1 width=76) (actual time=0.008..0.008 rows=0 loops=2025)

--                           Index Cond: (id = user_events.id)

--               ->  Index Scan using user_reset_password_events_pkey on user_reset_password_events  (cost=0.43..7.79 rows=1 width=32) (actual time=0.006..0.006 rows=0 loops=2025)

--                     Index Cond: (id = user_events.id)

--         ->  Index Scan using user_password_reset_request_created_event_pkey on user_password_reset_request_created_event  (cost=0.43..7.79 rows=1 width=32) (actual time=0.006..0.006 rows=0 loops=2025)

--               Index Cond: (id = user_events.id)

-- Planning Time: 0.763 ms

-- Execution Time: 46.283 ms
```

After CLUSTER (ALL TABLES):

```
Gather  (cost=1026.75..43431.50 rows=2142 width=208) (actual time=0.632..39.099 rows=2061 loops=1)
  Workers Planned: 1
  Workers Launched: 1
  ->  Nested Loop Left Join  (cost=26.75..42217.30 rows=1260 width=208) (actual time=0.271..20.856 rows=1030 loops=2)
        ->  Nested Loop Left Join  (cost=26.32..32531.89 rows=1260 width=176) (actual time=0.256..15.774 rows=1030 loops=2)
              ->  Nested Loop Left Join  (cost=25.89..22846.48 rows=1260 width=144) (actual time=0.239..10.711 rows=1030 loops=2)
                    ->  Nested Loop Left Join  (cost=25.47..13012.84 rows=1260 width=68) (actual time=0.218..5.622 rows=1030 loops=2)
                          ->  Parallel Bitmap Heap Scan on user_events  (cost=25.04..7915.67 rows=1260 width=52) (actual time=0.195..0.399 rows=1030 loops=2)
                                Recheck Cond: (user_id = 'd97abd46-8393-45fc-a8bc-0cb1547d50c2'::uuid)
                                Heap Blocks: exact=19
                                ->  Bitmap Index Scan on idx_36d54c77a76ed395  (cost=0.00..24.50 rows=2142 width=0) (actual time=0.322..0.323 rows=2061 loops=1)
                                      Index Cond: (user_id = 'd97abd46-8393-45fc-a8bc-0cb1547d50c2'::uuid)
                          ->  Index Only Scan using user_logged_in_events_pkey on user_logged_in_events  (cost=0.43..4.05 rows=1 width=16) (actual time=0.005..0.005 rows=0 loops=2061)
                                Index Cond: (id = user_events.id)
                                Heap Fetches: 0
                    ->  Index Scan using user_registered_events_pkey on user_registered_events  (cost=0.43..7.80 rows=1 width=76) (actual time=0.005..0.005 rows=0 loops=2061)
                          Index Cond: (id = user_events.id)
              ->  Index Scan using user_reset_password_events_pkey on user_reset_password_events  (cost=0.43..7.69 rows=1 width=32) (actual time=0.004..0.004 rows=0 loops=2061)
                    Index Cond: (id = user_events.id)
        ->  Index Scan using user_password_reset_request_created_event_pkey on user_password_reset_request_created_event  (cost=0.43..7.69 rows=1 width=32) (actual time=0.004..0.004 rows=0 loops=2061)
              Index Cond: (id = user_events.id)
Planning Time: 0.695 ms
Execution Time: 39.289 ms
```

