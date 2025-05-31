Execution [[Activity Timeouts]]:
- [[Schedule-To-Close]]
- [[Start-To-Close]]

After elapsing the [[Execution Timeouts|Execution Timeout]], the [[Activity]] is considered **Cancelled**. Any [[Activity Heartbeat]] attempt will throw `ActivityCanceledException`.

When using these timeouts, it's necessary to make sure that compensation logic covers rollback for the scenarios **when timed-out activity still succeeds**. 

Also, your [[Activity]] should be aware of the fact that **compensation logic could've already been executed** (and thus it must not attempt to succeed). [[Optimistic Locking]] should be used (version is read at the beginning of a transaction, and it'll fail if it has changed throughout the execution) - thus timed-out activity that knows nothing about being canceled must not corrupt the state of the application. Even using [[Activity Heartbeat]] before actual writing won't guarantee that at the moment of write compensation will not have been executed.

Beware that using [[Start-To-Close]] timeout in conjunction with [[Retry Policy]] for [[Activity|Activities]] that interact with **third-party [[Microservices|services]]** could result in **multiple requests** (two first being parallel) being sent to them if they take longer time to complete:
- one is sent from the [[Activity Task]] that eventually times-out (yet, after all this will succeed)
- another is sent from retried attempt (and will probably fail).

And due to the fact that second attempt has failed, third one will be launched (unless it failed with unretriable error, which would lead to the situation that task is completed, but activity failed), which'd result in the third attempt being sent to them, which will hopefully succeed due to [[Idempotence]].

In any case, these three attempts could've been avoided if [[Schedule-To-Close]] timeout had been used.

Anyhow, having an orchestrator is still a privilege, since we can set bigger timeout for http requests, and if one will succeed shortly after activity was timed-out, and new task won't be taken yet, successful result will be recorded in the database, and the next retry will succeed.
