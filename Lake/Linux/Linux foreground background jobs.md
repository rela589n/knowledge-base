To list current shell jobs, run `jobs`:

```shell
$ jobs

[1]   Running                 tail -f /dev/null &
[2]-  Running                 tail -f /dev/null &
[3]+  Stopped                 tail -f /dev/null
```

First `[id]` means Job ID.
Plus `+` means that the job is the most recent.
Minus `-` means that the job is the previous before the most recent.

You can **suspend** the foreground job with `Ctrl+Z` (it sends `SIGTSTP` to the program).

`bg` is used to put job into background: `bg %1`.
`fg` is used to put job into foreground: `fg %2`.

To **kill the job by ID**, run `kill %jobID`:

```shell
$ kill %2

[2]-  Stopped                 tail -f /dev/null
```
