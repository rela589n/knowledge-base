Create partitioned table:

```sql
create table user_events
(
    id        uuid         not null,
    user_id   uuid         not null
        constraint fk_36d54c77a76ed395
            references users,
    timestamp timestamp(6) not null,
    type      varchar(255) not null,
    primary key (user_id, id)
) partition by range (user_id);

create index idx_36d54c77a76ed395
    on user_events (user_id);
```

> Note that [[Primary Key]] is composite, because it's required to be so with [[Partitioning]] ([[Partitioning and Secondary Indexes]]).

Then, use script to [[Arrange data into Partitions#^d64a99|define partition boundaries]], and create [[Partition]] tables:

```sql
DO
$$
    DECLARE
        stmt TEXT;
    BEGIN
        FOR stmt IN (WITH boundaries AS (SELECT DISTINCT ON (partition) partition,
                                                                        lag(id, 1) OVER ()    AS start_id,
                                                                        last_value(id) OVER p AS end_id
                                         FROM (SELECT id,
                                                      ntile(2048) OVER (ORDER BY id) partition
                                               FROM users) parts
                                         WINDOW p AS (PARTITION BY partition)
                                         ORDER BY partition)
                     SELECT format(
                                    'CREATE TABLE user_events_p%s PARTITION OF user_events FOR VALUES FROM (%L) TO (%L);',
                                    lpad(partition::TEXT, 4, '0'),
                                    CASE
                                        WHEN partition = 1 THEN '00000000-0000-0000-0000-000000000000'::UUID
                                        ELSE start_id
                                        END,
                                    CASE
                                        WHEN partition = 2048 THEN 'ffffffff-ffff-ffff-ffff-ffffffffffff'::UUID
                                        ELSE end_id
                                        END
                            ) AS statement
                     FROM boundaries
                     ORDER BY partition)
            LOOP
                EXECUTE stmt;
                RAISE NOTICE 'Executed: %', stmt;
            END LOOP;
    END
$$
```

Once you've defined these, `user_events` table acts as a proxy for [[Partition]] tables so that you can select, insert, update, delete directly from this table.

Let's insert some data into it:

```sql
INSERT INTO user_events (id, user_id, timestamp, type)
SELECT uuid_generate_v4()                             as id,
       user_ids.ids[ceil(random() * user_ids.length)] as user_id,
       now() - (random() * INTERVAL '90 days')        as timestamp,
       types.values[ceil(random() * 10)]              as type
FROM (SELECT array_agg(id) as ids, count(id) as length FROM users) user_ids,
     (SELECT ARRAY ['login', 'register', 'password_reset_requested', 'password_reset', 'form_submit', 'file_upload', 'search', 'purchase', 'profile_update', 'password_change'] values) as types,
     generate_series(1, 20000000) as gen
;
```

Once it's there we can check how queries work with partitions.

```sql
EXPLAIN ANALYZE SELECT count(*) FROM user_events;
```

It results in a plan, similar to this:

```
Finalize Aggregate  (cost=378114.48..378114.49 rows=1 width=8) (actual time=2616.506..2628.255 rows=1 loops=1)
  ->  Gather  (cost=378114.26..378114.47 rows=2 width=8) (actual time=2609.666..2628.219 rows=3 loops=1)
        Workers Planned: 2
        Workers Launched: 2

        ->  Partial Aggregate  (cost=377114.26..377114.27 rows=1 width=8) (actual time=2437.270..2437.525 rows=1 loops=3)
              ->  Parallel Append  (cost=0.29..356280.93 rows=8333334 width=0) (actual time=237.442..2045.848 rows=6666670 loops=3)
                    ->  Parallel Index Only Scan using user_events_p0700_user_id_idx on user_events_p0700 user_events_700  (cost=0.29..160.66 rows=6074 width=0) (actual time=218.255..219.728 rows=10326 loops=1)
                          Heap Fetches: 0
                    ->  Parallel Index Only Scan using user_events_p1543_user_id_idx on user_events_p1543 user_events_1543  (cost=0.29..160.46 rows=6064 width=0) (actual time=215.559..216.654 rows=10308 loops=1)
                          Heap Fetches: 0
.....
                    ->  Parallel Index Only Scan using user_events_p1901_user_id_idx on user_events_p1901 user_events_1901  (cost=0.28..125.32 rows=4596 width=0) (actual time=0.383..1.382 rows=7814 loops=1)
                          Heap Fetches: 0
                    ->  Parallel Index Only Scan using user_events_p1847_user_id_idx on user_events_p1847 user_events_1847  (cost=0.28..125.21 rows=4591 width=0) (actual time=251.985..253.286 rows=7804 loops=1)
                          Heap Fetches: 0

Planning Time: 52.345 ms
JIT:
  Functions: 6152
"  Options: Inlining false, Optimization false, Expressions true, Deforming true"
"  Timing: Generation 98.187 ms (Deform 0.000 ms), Inlining 0.000 ms, Optimization 53.436 ms, Emission 654.294 ms, Total 805.917 ms"
Execution Time: 2406.799 ms
```

```sql
EXPLAIN ANALYZE
SELECT *
FROM user_events
WHERE user_id = '3f293879-05bb-4a95-9ae5-84e571537b37';
```

It uses only particular partition:

```
Bitmap Heap Scan on user_events_p0499 user_events  (cost=28.37..158.32 rows=2076 width=52) (actual time=0.100..0.812 rows=2076 loops=1)
  Recheck Cond: (user_id = '3f293879-05bb-4a95-9ae5-84e571537b37'::uuid)
  Heap Blocks: exact=104
  ->  Bitmap Index Scan on user_events_p0499_user_id_idx  (cost=0.00..27.86 rows=2076 width=0) (actual time=0.072..0.073 rows=2076 loops=1)
        Index Cond: (user_id = '3f293879-05bb-4a95-9ae5-84e571537b37'::uuid)
Planning Time: 0.604 ms
Execution Time: 0.980 ms
```

Note that simple search by id won't work quite well:

```sql
EXPLAIN ANALYZE
SELECT *
FROM user_events
WHERE id = '6deacbfa-2976-4ca7-853c-1152804eb542';
```

It uses [[Scatter-gather]]:
```
Gather  (cost=1000.00..355967.94 rows=2048 width=52) (actual time=1844.305..1862.651 rows=1 loops=1)
  Workers Planned: 2
  Workers Launched: 2

  ->  Parallel Append  (cost=0.00..354763.14 rows=2048 width=52) (actual time=1582.884..1664.858 rows=0 loops=3)
        ->  Parallel Seq Scan on user_events_p0700 user_events_700  (cost=0.00..182.93 rows=1 width=52) (actual time=1278.177..1278.178 rows=0 loops=1)
              Filter: (id = '6deacbfa-2976-4ca7-853c-1152804eb542'::uuid)
              Rows Removed by Filter: 10326
...
        ->  Parallel Seq Scan on user_events_p1847 user_events_1847  (cost=0.00..138.38 rows=1 width=52) (actual time=1187.472..1187.472 rows=0 loops=1)
              Filter: (id = '6deacbfa-2976-4ca7-853c-1152804eb542'::uuid)
              Rows Removed by Filter: 7804

Planning Time: 48.363 ms
JIT:
  Functions: 12288
"  Options: Inlining false, Optimization false, Expressions true, Deforming true"
"  Timing: Generation 358.246 ms (Deform 124.533 ms), Inlining 0.000 ms, Optimization 166.301 ms, Emission 3311.739 ms, Total 3836.285 ms"
Execution Time: 1907.626 ms
```

It's run in parallel because data's partitioned by `user_id`, and it's required to know which partition to send the request to. Besides that, it's [[Sequence Scan]] that is used.

Thus, it works fine only when `user_id` is part of the filter:

```sql
EXPLAIN ANALYZE
SELECT *
FROM user_events
WHERE user_id = '5f45c5a3-0c08-47a9-9b89-e21cdaa952c3'
    AND id = '6deacbfa-2976-4ca7-853c-1152804eb542';
```

```
Index Scan using user_events_p0746_pkey on user_events_p0746 user_events  (cost=0.29..8.30 rows=1 width=52) (actual time=1.382..1.386 rows=1 loops=1)
  Index Cond: ((user_id = '5f45c5a3-0c08-47a9-9b89-e21cdaa952c3'::uuid) AND (id = '6deacbfa-2976-4ca7-853c-1152804eb542'::uuid))
Planning Time: 0.162 ms
Execution Time: 1.410 ms
```

If you really need to search by ID, consider either changing the order of [[Primary Key]], or adding [[Secondary Index]].

```sql
EXPLAIN ANALYZE
SELECT * FROM user_events ORDER BY user_id
LIMIT 10;
```

With this query some Index scans are never executed.

It's possible to create [[Foreign Key]] toward the partitioned table:

```sql
CREATE TABLE user_event_details
(
    event_id uuid NOT NULL,
    user_id  uuid NOT NULL,
    details  jsonb,
    CONSTRAINT fk_user_events
        FOREIGN KEY (user_id, event_id)
            REFERENCES user_events (user_id, id)
            ON DELETE CASCADE,
    PRIMARY KEY (event_id)
);

INSERT INTO user_event_details (event_id, user_id, details)
SELECT id, user_id, '{}'::JSONB AS details
FROM user_events TABLESAMPLE bernoulli(1)
LIMIT 10;
```

It fully controls that values in `user_event_details` will have the corresponding values in Partitioned `user_events` table.

See also [[pg_partman]] for automatic management of partitions.
