You can set up container with [[Var dump server]], and then analyse logs with [[Lnav]]:

```shell
docker compose logs --no-log-prefix -f dump_server | lnav
```