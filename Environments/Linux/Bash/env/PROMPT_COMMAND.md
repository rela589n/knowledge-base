Controls what is executed every time any command is executed.

If you set it,
```shell
PROMPT_COMMAND='echo -n "writing the prompt at " && date'
```

And then run any command, this `PROMPT_COMMAND` will be executed as well.

This can be used for example in [[Docker]] container in order to save the history right away:

```shell
PROMPT_COMMAND="history -a;$PROMPT_COMMAND"
```