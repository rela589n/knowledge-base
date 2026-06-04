```sql
CREATE USER readonly_local WITH PASSWORD 'your-password';
GRANT CONNECT ON DATABASE "your-database-name" TO readonly_local;
GRANT USAGE ON SCHEMA public TO readonly_local;

GRANT SELECT ON ALL TABLES IN SCHEMA public TO readonly_local;
GRANT SELECT ON ALL SEQUENCES IN SCHEMA public TO readonly_local;
```

Verify that the user exists:
```sql
SELECT 1 FROM pg_roles WHERE rolname='readonly_local';
```