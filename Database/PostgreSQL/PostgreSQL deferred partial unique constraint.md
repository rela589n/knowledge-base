This will create partial unique deferred constraint:

```sql
ALTER TABLE table_name
    ADD CONSTRAINT table_name_uniq
        EXCLUDE USING btree (some_field WITH =, another_field WITH =)
        WHERE (deleted_at IS NULL)
        DEFERRABLE INITIALLY DEFERRED;
```
