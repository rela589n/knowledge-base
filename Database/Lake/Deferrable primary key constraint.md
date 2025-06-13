In [[PostgreSQL]] it's possible to create it:

```sql
ALTER TABLE files
    DROP CONSTRAINT files_pkey;  
  
ALTER TABLE files  
    ADD PRIMARY KEY (id) DEFERRABLE INITIALLY DEFERRED;
```

But later on it won't be possible to have a foreign key to this table.

This will fail:
```sql
ALTER TABLE warehouses  
ADD CONSTRAINT FK_B5871404A8DBFD92 FOREIGN KEY (file_id) REFERENCES files (id) DEFERRABLE INITIALLY DEFERRED
```

With errror:
> [55000] ERROR: cannot use a deferrable unique constraint for referenced table "files"

