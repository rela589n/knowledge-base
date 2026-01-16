Having set `VAR_DUMPER_FORMAT: server`, you could use separate var-dump server:

```shell
./vendor/bin/var-dump-server
```


To run [[Var dump server]] from the [[Docker]] container, use:

```shell
./vendor/bin/var-dump-server --no-anisi > var/log/dump.log &
exit
```

This will output dumps into the file, so you can analyse it with [[Lnav]].

Also, see [buggregator/trap](https://github.com/buggregator/trap) which provides better DX.
