---
aliases:
  - Hot Update Example
---
[[HOT update]] test that shows that when [[Database Index|Index]] changes, the actual update must re-evaluate all [[Database Index|Indexes]], including [[Expression-based Index|Expression-based Indexes]]:

```sql
-- Function that sleeps and logs when called
CREATE OR REPLACE FUNCTION track_calls(val TEXT) RETURNS TEXT AS $$
BEGIN
    RAISE NOTICE 'Function called with: % at %', val, now();
    PERFORM pg_sleep(2);
    RETURN upper(val);
END;
$$ LANGUAGE plpgsql IMMUTABLE;

select track_calls('foo bar');

CREATE TABLE test (id INT, name TEXT, email TEXT);
INSERT INTO test VALUES (1, 'john', 'old@email.com');

-- Simple index
CREATE INDEX test_email_idx ON test (email);

-- Expression index
CREATE INDEX test_name_idx ON test (track_calls(name));

-- Test: update email (not in expression, but used in another index)
UPDATE test SET email = 'new@email.com' WHERE id = 1;
-- [2025-07-05 17:35:21] 1 row affected in 2 s 43 ms 🤯

-- HOT update performed quickly (no index changes)
UPDATE test SET id = 2 WHERE id = 1;
UPDATE test SET id = 1 WHERE id = 2;
-- [2025-07-05 17:36:27] 1 row affected in 8 ms

-- Check HOT stats
SELECT n_tup_hot_upd FROM pg_stat_user_tables WHERE relname = 'test';
```