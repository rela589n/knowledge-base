**Start-To-Close** [[Activity Timeouts|Activity Timeout]] (recommended) - timeout for a single [[Activity Task]] execution.

If first [[Worker]] started [[Activity]] execution, and it didn't manage to complete within a timeout time, a next attempt is launched.


![[Start-To-Close Timeout.png#center|500]]

When using this timeout, it's necessary to make sure that compensation covers rollback for the scenario **if timed-out activity eventually succeeds**.

Beware using that this kind of timeout with third-party services that take long time to complete could result in **multiple requests** (two first being parallel) being sent to them:
- one had been sent from an already timed-out [[Activity Task]] (after all, this will succeed)
- another from retried attempt (this will probably fail).

And due to the fact that second attempt has failed, third one will be launched (unless it failed with unretriable error, which would lead to the situation that task is completed, but activity failed), which'd result in the third attempt being sent to them, which will hopefully succeed due to [[Idempotence]].

In any case, these three attempts could've been avoided had [[Schedule-To-Close]] timeout been used.

Anyhow, having an orchestrator is a big privilege, since we can set bigger timeout for http requests, and if one will succeed shortly after activity was timed-out, and new task won't be taken yet, successful result will be recorded in the database, and the next retry will succeed.
