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
