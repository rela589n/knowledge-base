---
aliases:
  - Cancel a Workflow
---
[[Temporal/Workflow/Workflow|Workflow]] Cancellation is a graceful shutdown (anticipates cleanup) of [[Workflow Execution]].

When you cancel the workflow, [[Server]] records an [[Workflow Event|Event]], so that [[Activity Heartbeat]] will fail (as if [[Activity Cancellation]]), and [[Workflow Task]] is scheduled so that an `CanceledFailure` exception is thrown from the [[Temporal/Workflow/Workflow|Workflow]] itself. Thus, if it defines [[SAGA|compensations]], they'll be executed (make sure to use `Saga` object, lest you'll find out [[Compensation is not executed during Cancellation]] problem).

[[Temporal CLI Cancel Workflow]]