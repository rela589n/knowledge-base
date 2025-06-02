---
aliases:
  - Cancel a Workflow
---
[[Temporal/Workflow/Workflow|Workflow]] Cancellation is a graceful shutdown (anticipates cleanup) of [[Workflow Execution]].

When you cancel the workflow, [[Server]] records an [[Workflow Event|Event]], so that [[Activity Heartbeat]] will fail (as if [[Activity Cancellation]]). 

[[Workflow Task]] is scheduled so that an `CanceledFailure` exception is thrown from the [[Temporal/Workflow/Workflow|Workflow]] itself on the last point. 

If [[Temporal/Workflow/Workflow|Workflow]] defines [[SAGA|compensations]], they'll be executed if properly configured (use `Saga` object lest you face [[Compensation is not executed during Cancellation]] problem).

Also, know that in this case [[Compensation is executed before Activity is Completed]]. Since activity has some particular [[Activity Heartbeat Timeout|Heartbeat Timeout]], and interval within which it heartbeats, workflow compensations are executed before it's completion.

[[Temporal CLI Cancel Workflow]]