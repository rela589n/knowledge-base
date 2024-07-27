## Logs

View logs from server, app, etc:

```bash
sf server:log
```

## Env

Manage env in `.env.local`. 
See vars exposed by sf: `symfony var:export`
The `.env.local.php` can be used in prod. To dump: `composer dump-env`.



## Dump

```bash
symfony run pg_dump --data-only > dump.sql
```

```
symfony run psql < dump.sql
```


## Workers

To run workers in background:

```
symfony run -d --watch=config,src,templates,vendor symfony console messenger:consume async -vv
```