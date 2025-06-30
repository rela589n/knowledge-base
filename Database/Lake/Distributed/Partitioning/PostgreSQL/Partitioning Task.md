Model aggregate and inner entities.

Make sure that inner entities are partitioned by the parent id (classic one-to-many).

Insert few thousand aggregates, and few million inner entities.

Analyse performance of inner queries, and compare it to ordinary approach with just two tables.

That's actually interesting story about Composition. It would be cool if it worked better because only one particular predetermined table is needed to be scanned, not the whole table over all aggregates.
Partitioned data is goodly stored on disk (no random access, everything is in place)

Check how hash indexes work.

> **TLDR**
> 
> Use Partitions only if you have up to few thousand of them.

## Test - Level 1

This test is performed with the following setup:
- users table: 10_000 records;
- accounts table (partitioned by user id): 3_000_000 records;

Each user has his own accounts table (e.g. totally there are 10k tables).

### Setup

Create users table:

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

CREATE SEQUENCE IF NOT EXISTS users_sequence_id_seq;

ALTER TABLE users
    ADD COLUMN sequence_id BIGINT DEFAULT nextval('users_sequence_id_seq') NOT NULL;

ALTER TABLE users
    ADD CONSTRAINT users_sequence_id_unique UNIQUE (sequence_id);
```

Create accounts (Not Partitioned) Table:

```sql
create table accounting_accounts_not_partitioned
(
    id          uuid         not null,
    sequence_id bigserial    not null unique,
    user_id     uuid         not null,
    number      integer      not null,
    created_at  timestamp(6) not null,
    updated_at  timestamp(6) not null,
    primary key (user_id, id)
)
```

Insert those records:

```sql
INSERT INTO accounting_accounts_not_partitioned (id, user_id, number, created_at, updated_at)
SELECT uuid_generate_v4()                             as id,
       user_ids.ids[ceil(random() * user_ids.length)] as user_id,
       floor(random() * 9000000 + 1000000)::integer   as number, -- Random 7-digit account numbers
       now() - (random() * INTERVAL '365 days')       as created_at,
       now() - (random() * INTERVAL '30 days')        as updated_at
FROM (SELECT array_agg(id) as ids, count(id) as length FROM users) user_ids,
     generate_series(1, 3000000) as gen -- 3 million records
;
```

Create Partitioned table:

```sql
create table accounting_accounts
(
    id          uuid         not null,
    sequence_id bigint       not null,
    user_id     uuid         not null,
    number      integer      not null,
    created_at  timestamp(6) not null,
    updated_at  timestamp(6) not null,
    primary key (user_id, id)
)
    partition by LIST (user_id);
```

Create Partitions using [[Async Partitions setup Script]]

Insert partitions data:

```sql
INSERT INTO accounting_accounts (id, sequence_id, user_id, number, created_at, updated_at)  
SELECT id, sequence_id, user_id, number, created_at, updated_at  
FROM accounting_accounts_not_partitioned order by sequence_id;
```

Run [[PostgreSQL VACUUM|VACUUM]]:

```sql
VACUUM ANALYZE;
```

### Observation

`Vacuum Analyze` becomes quite slow (?)

`max_locks_per_transaction` = 1000 - it was necessary to increase, because if query touches many partitions, it runs out of locks.

Partitioned Tables size is much bigger - almost three times.
(991 MB vs 384 MB)

Count queries (on the full table), and other queries, that analyze many partitions are extremely slow with partitions.

In performance comparison with not partitioned, it turns out to be that Planning Time is greater (it needs to analyse what partition to use), but execution is real fast.

### Select by User ID

Partitioned:

```sql
EXPLAIN ANALYZE
SELECT * FROM accounting_accounts
         WHERE user_id = 'fd5bb62f-b409-42d9-8ebb-7b931226fead';
```

```
Seq Scan on accounting_accounts_p5644 accounting_accounts  (cost=0.00..7.80 rows=304 width=52) (actual time=0.014..0.052 rows=304 loops=1)
  Filter: (user_id = 'fd5bb62f-b409-42d9-8ebb-7b931226fead'::uuid)

Planning Time: 0.230 ms
Execution Time: 0.074 ms
```

Not Partitioned:

```sql
EXPLAIN ANALYZE
SELECT * FROM accounting_accounts_not_partitioned
         WHERE user_id = '3467ec5e-f96f-4a18-9b2f-0862e3d3eb05';
```

```
Bitmap Heap Scan on accounting_accounts_not_partitioned  (cost=10.87..1118.86 rows=299 width=52) (actual time=0.198..1.596 rows=345 loops=1)
  Recheck Cond: (user_id = '7d017366-50ef-452b-994a-e4efe6d2a363'::uuid)
  Heap Blocks: exact=343
  ->  Bitmap Index Scan on accounting_accounts_not_partitioned_pkey  (cost=0.00..10.80 rows=299 width=0) (actual time=0.118..0.119 rows=345 loops=1)
        Index Cond: (user_id = '7d017366-50ef-452b-994a-e4efe6d2a363'::uuid)

Planning Time: 0.097 ms
Execution Time: 1.643 ms
```

Thus, `0.3 ms` vs `1.7 ms` - **Partitioned is about 5 times faster**. Yet, it's not substantial because these are but milliseconds.

#### Range query by user ID (20 users)

Partitined:

```
Append  (cost=0.03..107.68 rows=3319 width=52) (actual time=0.020..1.044 rows=3319 loops=1)
...
  ->  Seq Scan on accounting_accounts_p4315 accounting_accounts_3  (cost=0.03..8.74 rows=314 width=52) (actual time=0.011..0.092 rows=314 loops=1)
"        Filter: (user_id = ANY ('{...}'::uuid[]))"
...
Planning Time: 1.728 ms
Execution Time: 2.125 ms
```

Not partitioned:

```
Bitmap Heap Scan on accounting_accounts_not_partitioned  (cost=217.49..15241.60 rows=5975 width=52) (actual time=2.738..21.383 rows=6029 loops=1)
"  Recheck Cond: (user_id = ANY ('{...}'::uuid[]))"
  Heap Blocks: exact=5501
  ->  Bitmap Index Scan on accounting_accounts_not_partitioned_pkey  (cost=0.00..215.95 rows=5975 width=0) (actual time=1.537..1.538 rows=6029 loops=1)
"        Index Cond: (user_id = ANY ('{...}'::uuid[]))"
Planning Time: 0.145 ms
Execution Time: 21.729 ms
```

Thus, `3.85ms` vs `21.87ms` - the same result. 

**Partitioned is five times faster**.

Yet, keep in mind table size overhead.

### Test 2

Create Non-Partitioned Table (around 20 mins):

```sql
create table accounting_account_transactions_not_partitioned  
(  
    id          uuid         not null,  
    amount      integer      not null,  
    description varchar(255) not null,  
    created_at  timestamp(6) not null,  
    account_id  uuid,  
    primary key (account_id, id)  
);

INSERT INTO accounting_account_transactions_not_partitioned (id, amount, description, created_at, account_id)
SELECT uuid_generate_v4()                                as id,
       floor(random() * 199999 - 99999)::integer         as amount,
       'Transaction #' || gen                             as description,
       now() - (random() * INTERVAL '365 days')          as created_at,
       account_ids.ids[ceil(random() * account_ids.length)] as account_id
FROM (SELECT array_agg(id) as ids, count(id) as length FROM accounting_accounts_not_partitioned) account_ids,
     generate_series(1, 30000000) as gen -- 30 million records

CREATE SEQUENCE IF NOT EXISTS accounting_account_transactions_sequence_id_seq;

ALTER TABLE accounting_account_transactions_not_partitioned
    ADD COLUMN sequence_id BIGINT DEFAULT nextval('accounting_account_transactions_sequence_id_seq') NOT NULL;

ALTER TABLE accounting_account_transactions_not_partitioned
    ADD CONSTRAINT accounting_account_transactions_sequence_id_unique UNIQUE (sequence_id);
```

Create Partitioned table:

```sql
create table accounting_account_transactions
(
    id          uuid         not null,
    amount      integer      not null,
    description varchar(255) not null,
    sequence_id bigint       not null,
    created_at  timestamp(6) not null,
    account_id  uuid,
    primary key (account_id, id)
)
    partition by LIST (account_id);
```

Setup Partitions with [[Async Partitions setup Script]]

Fill Partitioned Table.


