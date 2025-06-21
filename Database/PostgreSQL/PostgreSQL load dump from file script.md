```bash
cat dump.sql | docker compose exec -T --env PGPASSWORD=qwerty postgresql psql -h postgresql -U postgres "database-name"
```

Or with `zcat`:
```shell
zcat ./table-dump.sql.gz | docker compose exec -T --env PGPASSWORD=qwerty postgresql_container psql -h postgresql_container -U postgres_user "database_name"
```