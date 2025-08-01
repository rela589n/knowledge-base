---
aliases:
  - Execution Timeout
---
Execution [[Activity Timeouts]]:
- [[Schedule-To-Close]]
- [[Start-To-Close]]

> Most of the time [[Start-To-Close]] timeout is more predictable than [[Schedule-To-Close]]. When it's something critical, it's better to use [[Start-To-Close]] rather than [[Schedule-To-Close]] so that it will be retried as many times as needed.

After elapsing the [[Activity Execution Timeouts|Execution Timeout]], the [[Activity]] is marked as [[Activity Cancellation|Cancelled]]. Any [[Activity Heartbeat]] attempt will throw `ActivityCanceledException`.

When using those timeouts, it's necessary to make sure that compensation logic covers rollback for the scenarios **when timed-out activity still succeeds**. 

Also, your [[Activity]] should be aware of the fact that **compensation logic could've already been executed** (and thus it must not attempt to succeed). If it doesn't involve third-parties, [[Optimistic Locking]] can be used (version is read at the beginning of a transaction, and it'll fail if it has changed throughout the execution (compensation would've changed it)) - thus timed-out [[Activity]] that isn't aware that it was canceled will not corrupt the state of the application. Even using [[Activity Heartbeat]] before the actual writing won't guarantee that at the moment of write compensation will not have been executed, and also it's prone to [[Activity Heartbeat Throttling|Throttling]], and may not arrive to the [[Temporal/Temporal Server|Server]] if [[Activity Execution Timeouts|Execution Timeout]] hasn't elapsed.

See [[Compensation is executed before Activity actually Completes]]

Beware that using [[Start-To-Close]] timeout in conjunction with [[Retry Policy]] for [[Activity|Activities]] that interact with **third-party [[Microservices|services]]** could result in **multiple requests** (two first being parallel) being sent to them if they take longer time to complete:
- one is sent from the [[Activity Task]] that eventually times-out (yet, after all this will succeed)
- another is sent from retried attempt (and will probably fail).

And due to the fact that second attempt has failed, third one will be launched (unless it failed with unretriable error, which would lead to the situation that task is completed, but activity failed), which'd result in the third attempt being sent to them, which will hopefully succeed due to [[Idempotence]].

To fix this, make sure to design the system in such way that [[Start-To-Close]] timeout incorporates http timeout, so that [[Activity|Activities]] would have no chance of being timed-out, and still alive. 

And then, make sure to increase [[Activity Retry Options#^0cd43f|initial delay]] so that previous request will have chance to complete on the upstream side before the next request is sent. In any case it's better than sending the request right away.

In any case, these three attempts could've been avoided if [[Schedule-To-Close]] timeout had been used.

Anyhow, having an orchestrator is still a privilege, since we can set bigger timeout for http requests, and if one will succeed shortly after activity was timed-out, and new task won't be taken yet, successful result will be recorded in the database, and the next retry will succeed.
