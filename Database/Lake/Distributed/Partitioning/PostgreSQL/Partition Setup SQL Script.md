```sql
DO
$$
    DECLARE
        stmt TEXT;
    BEGIN
        FOR stmt IN (WITH boundaries AS (SELECT sequence_id, id from users)
                     SELECT format(
                                    'CREATE TABLE IF NOT EXISTS accounting_accounts_p%s PARTITION OF accounting_accounts FOR VALUES IN (%L);',
                                    sequence_id,
                                    id
                            ) AS statement
                     FROM boundaries
                     ORDER BY sequence_id)
            LOOP
                EXECUTE stmt;
                RAISE NOTICE 'Executed: %', stmt;
            END LOOP;
    END
$$
```
