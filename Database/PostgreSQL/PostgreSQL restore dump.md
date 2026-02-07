```bash
#!/bin/bash
set -e

DUMP_FILE="/path/to/dump-file.sql"
DB_NAME="your-db-name-prod"

docker compose exec postgresql psql -U postgres -c "DROP DATABASE IF EXISTS \"$DB_NAME\";"
docker compose exec postgresql psql -U postgres -c "CREATE DATABASE \"$DB_NAME\";"
cat "$DUMP_FILE" | docker compose exec -T postgresql psql -U postgres -d "$DB_NAME"
```
