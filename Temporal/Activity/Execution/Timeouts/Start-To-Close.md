**Start-To-Close** [[Activity Timeouts|Activity Timeout]] (recommended) - timeout for a single [[Activity Task]] execution.

If first [[Worker]] started [[Activity]] execution, and it didn't manage to complete within a timeout time, a next attempt is launched.


![[Start-To-Close Timeout.png#center|500]]

Beware using that this kind of timeout with third-party services that take long time to complete could result in **multiple requests** (two first being parallel) sent to them:
- one from already timed-out (after all this will succeed)
- another from retried attempt (this will probably fail).

And due to the second attempt being failed, third one will be launched (unless second failed with unretriable error), which'd result in the third attempt being sent to them, which will hopefully succeed ([[Idempotence]]).

In any case, these three attempts could've been avoided had [[Schedule-To-Close]] timeout been used.

Anyway, having an orchestrator is a big privilege, since we could set bigger timeout for http requests, and if one will succeed shortly after activity was timed-out, it'll be recorded in the database so that next retry will succeed (in case it happens before sending repetitive request).

