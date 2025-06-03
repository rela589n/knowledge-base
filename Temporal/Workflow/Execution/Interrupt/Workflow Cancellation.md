---
aliases:
  - Cancel a Workflow
---
[[Temporal/Workflow/Workflow|Workflow]] Cancellation is a graceful shutdown (anticipates cleanup) of [[Workflow Execution]].

When you cancel the workflow, [[Temporal Server]] records `WorkflowExecutionCancelRequested` [[Workflow Event|Event]], and schedules [[Workflow Task]] to [[Workflow Replay|Replay the Workflow]]  to its last [[Workflow Execution|Execution]] point, and causes its unfinished child task to be cancelled (and cause it to be propagated into [[Activity Cancellation|Activity Cancellations]]), and finally it throws cancellation exception from any following yielded operation (and thus [[Workflow Async Operations#^c4a0d6|Workflow::asyncDetached()]] should be used in `catch` block to run [[SAGA|compensations]]).

If [[Temporal/Workflow/Workflow|Workflow]] defines any [[SAGA|compensations]], they'll be executed if they are properly configured (using `Saga` object, because otherwise [[Compensation is not executed during Cancellation]] problem rises up).

Depending on the [[#^7f674b|Activity cancellationType]], it may throw either `CanceledFailure` (default), or an `ActivityFailure` with either `previous=CanceledFailure` or `previous=TimeoutFailure`.

It's up to [[Temporal/Workflow/Workflow Definition|Workflow Code]] to handle cancellation request, or to ignore it. Know that if it throws retryable `\Error`, actually it won't be cancelled per se, because it results in [[Workflow Task Failure]], which is retried, and it will proceed further.

> [[Activity Heartbeat]] does not fail right away after recording cancellation request to the [[Event History]]. It only fails after [[Workflow Task]] has sent [[Activity Cancellation]] request to the running activities.

Due to this, know that during Cancellation there can be a problem that [[Compensation is executed before Activity actually Completes]]. Since [[Activity]] has some particular [[Activity Heartbeat Timeout|Heartbeat Timeout]], and it heartbeats within that interval, scheduled workflow [[SAGA|compensations]] are likely to be executed before [[Activity]] completes with [[Activity Heartbeat#^e33915|heartbeat failure]].

It is possible to set [[Activity cancellationType|cancellationType]]=wait in order to wait until the next [[Activity Heartbeat|Heartbeat]] is reported to the [[Activity]] so that it'll accept the cancellation and thus  [[Temporal/Workflow/Workflow|Workflow's]] `catch` block will be executed in the next [[Workflow Task]] only after [[Activity]] has processed the cancellation (or after the [[Activity Heartbeat Timeout|Heartbeat has Timed-out]], - due to crash or any other cause). ^7f674b

What happens if activity dies, and `cancellationType=wait`? heartbeat timeout kicks in

Is it thrown on timers when activity's `cancellationType=wait`? yes

When [[Workflow Execution]] is cancelled, It depends on `cancellationType` [[Activity Options]].


Only after [[Workflow Execution]] has thrown `CanceledFailure` will [[Temporal Server|Temporal Service]] cause [[Activity Heartbeat]]s to fail (as if [[Activity Cancellation]]).


Also, beware of [[CanceledFailure exception is never thrown when using Workflow Async operations]] problem, and use `yield` everywhere you can 🙂.

[[Temporal CLI Cancel Workflow]]