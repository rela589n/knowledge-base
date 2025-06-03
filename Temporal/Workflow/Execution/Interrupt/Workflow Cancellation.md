---
aliases:
  - Cancel a Workflow
---
[[Temporal/Workflow/Workflow|Workflow]] Cancellation is a graceful shutdown (anticipates cleanup) of [[Workflow Execution]].

When you cancel the workflow, [[Temporal Server]] records `WorkflowExecutionCancelRequested` [[Workflow Event|Event]], that will cause [[Workflow Task]] to be scheduled so that from the last point of [[Workflow Execution]] `CanceledFailure` is thrown on any further yielded operation (and therefore [[Workflow Async Operations#^c4a0d6|Workflow::asyncDetached()]] should be used in `catch` block).

> [[Activity Heartbeat]] does not fail right away after recording cancellation request. It only fails after [[Workflow Task]] has thrown `CanceledFailure` (it may not throw it).

It's up to [[Temporal/Workflow/Workflow Definition|Workflow Code]] to handle cancellation request, or to ignore it. Know that if it throws retryable `\Error`, actually it won't be cancelled per se, but it will be retried ([[Workflow Task Failure]]s are retried) and proceed.

If [[Temporal/Workflow/Workflow|Workflow]] defines any [[SAGA|compensations]], they'll be executed if they are properly configured (using `Saga` object, because otherwise [[Compensation is not executed during Cancellation]] problem will rise up).

Only after [[Workflow Execution]] has thrown `CanceledFailure` will [[Temporal Server|Temporal Service]] cause [[Activity Heartbeat]]s to fail (as if [[Activity Cancellation]]).

Due to this, know that during Cancellation [[Compensation is executed before Activity actually Completes]]. Since [[Activity]] has some particular [[Activity Heartbeat Timeout|Heartbeat Timeout]], and it heartbeats within that interval, scheduled workflow [[SAGA|compensations]] are likely to be executed before [[Activity]] completes with [[Activity Heartbeat#^e33915|heartbeat failure]].

Also, beware of [[CanceledFailure exception is never thrown when using Workflow Async operations]] problem, and use `yield` everywhere you can 🙂.

[[Temporal CLI Cancel Workflow]]