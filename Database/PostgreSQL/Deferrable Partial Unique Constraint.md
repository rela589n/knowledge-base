In [[PostgreSQL]] this will create partial unique [[Deferrable Constraint]] (using [[PostgreSQL Exclude Constraint|EXCLUDE]]):

```sql
ALTER TABLE table_name
    ADD CONSTRAINT table_name_uniq
        EXCLUDE USING btree (some_field WITH =, another_field WITH =)
        WHERE (deleted_at IS NULL)
        DEFERRABLE INITIALLY DEFERRED;
```
