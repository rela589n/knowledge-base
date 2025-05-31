Execution [[Activity Timeouts]]:
- [[Schedule-To-Close]]
- [[Start-To-Close]]

When using these timeouts, it's necessary to make sure that compensation logic covers rollback for the scenarios **when timed-out activity still succeeds**.

Beware that using [[Start-To-Close]] timeout in conjunction with [[Retry Policy]] for [[Activity|Activities]] that interact with **third-party [[Microservices|services]]** could result in **multiple requests** (two first being parallel) being sent to them if they take longer time to complete:
- one is sent from the [[Activity Task]] that eventually times-out (yet, after all this will succeed)
- another is sent from retried attempt (and will probably fail).

And due to the fact that second attempt has failed, third one will be launched (unless it failed with unretriable error, which would lead to the situation that task is completed, but activity failed), which'd result in the third attempt being sent to them, which will hopefully succeed due to [[Idempotence]].

In any case, these three attempts could've been avoided if [[Schedule-To-Close]] timeout had been used.

Anyhow, having an orchestrator is still a privilege, since we can set bigger timeout for http requests, and if one will succeed shortly after activity was timed-out, and new task won't be taken yet, successful result will be recorded in the database, and the next retry will succeed.
