```shell
ping db-host          # Checks if host is alive
telnet db-host 5432   # Checks if PgSQL is listening
```

Ping uses ICMP, which could be blocked for security reasons.

Telnet uses TCP.

NetCat also supports UDP.

