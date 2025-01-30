```bash
cat dump.sql | docker compose exec -T --env PGPASSWORD=qwerty postgresql psql -h postgresql -U postgres "database-name"
```

