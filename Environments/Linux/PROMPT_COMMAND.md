Controls what is executed every time any command is executed.

If you set it,
```shell
PROMPT_COMMAND='echo -n "writing the prompt at " && date'
```

And then run any command, this `PROMPT_COMMAND` will be executed as well.
