---
aliases:
  - Cancel the Workflow
---
[[Temporal/Workflow/Workflow|Workflow]] Cancellation is a graceful shutdown (anticipates cleanup) of [[Workflow Execution]].

When you cancel the workflow, [[Temporal/Temporal Server]] records `WorkflowExecutionCancelRequested` [[Workflow Event|Event]], and schedules [[Workflow Task]] to [[Workflow Replay|Replay the Workflow]]  to its last [[Workflow Execution|Execution]] point, and causes its unfinished child task to be cancelled (and cause it to be propagated into [[Activity Cancellation|Activity Cancellations]]), and finally it throws cancellation exception from any following yielded operation (and thus [[Workflow Async Operations#^c4a0d6|Workflow::asyncDetached()]] should be used in `catch` block to run [[SAGA|compensations]]).

If [[Temporal/Workflow/Workflow|Workflow]] defines any [[SAGA|compensations]], they'll be executed if they are properly configured (using `Saga` object, because otherwise [[Compensation is not executed during Cancellation]] problem rises up).

Depending on the [[#^7f674b|Activity cancellationType]], it may throw either `CanceledFailure` (default), or an `ActivityFailure` with either `previous=CanceledFailure` or `previous=TimeoutFailure`.

It's up to [[Temporal/Workflow/Workflow Definition|Workflow Code]] to handle cancellation request, or to ignore it. Know that if it throws retryable `\Error`, actually it won't be cancelled per se, because it results in [[Workflow Task Failure]], which is retried, and it will proceed further.

> [[Activity Heartbeat]] does not fail right away after recording cancellation request to the [[Event History]]. It only fails after [[Workflow Task]] has sent [[Activity Cancellation]] request to the running activities.

Due to this, know that during Cancellation there can be a problem that [[Compensation is executed before Activity actually Completes]]. Since [[Activity]] has some particular [[Activity Heartbeat Timeout|Heartbeat Timeout]], and it heartbeats within that interval, scheduled workflow [[SAGA|compensations]] are likely to be executed before [[Activity]] completes with [[Activity Heartbeat#^e33915|heartbeat failure]].

It is possible to set [[Activity cancellationType|cancellationType]]=wait in order to wait until the next [[Activity Heartbeat|Heartbeat]] is reported to the [[Activity]] so that it'll accept the cancellation and thus  [[Temporal/Workflow/Workflow|Workflow's]] `catch` block will be executed in the next [[Workflow Task]] only after [[Activity]] has processed the cancellation (or after the [[Activity Heartbeat Timeout|Heartbeat has Timed-out]], - due to crash or any other cause). ^7f674b

In case if [[Activity Heartbeat Timeout|Heartbeat Timeout]] isn't specified, the [[Activity Cancellation|Activity will still be marked for Cancelling]], yet due to the [[Activity Heartbeat Throttling|Heartbeat Throttling]] none of the [[Activity Heartbeat|Heartbeats]] will be sent to the [[Temporal/Temporal Server|Service]], so the current [[Activity]] is only awaited until it's [[Activity Execution Timeouts|Execution Timeout]] (or until it completes), after which Workflow compensations are triggered. And from [[Activity]]'s POV once it's timed-out, the [[Activity Heartbeat|Heartbeat]] will be sent to the [[Temporal/Temporal Server|Service]], so it would stop.

To recap, in simplest case, when [[Workflow Cancellation]] is requested, it just marks [[Activity Cancellation|Activity for Cancellation]], and throws `CanceledFailure` right away. Otherwise If activity defines [[Activity cancellationType|cancellationType]], but it doesn't [[Activity Heartbeat|Heartbeat]], it's awaited until completion (or [[Activity Execution Timeouts|Execution Timeout]]). Else if it does [[Activity Heartbeat|Heartbeat]], [[Temporal/Workflow/Workflow|Workflow]] waits for this [[Activity Heartbeat|Heartbeat]] to throw (or until [[Activity Heartbeat Timeout|Heartbeat Timeout]]). In either case, if the activity is not last, or if it didn't complete successfully, exception is throw and [[SAGA|compensations]] are executed. Otherwise [[Workflow Execution]] is successful.

Also, beware of [[CanceledFailure exception is never thrown when using Workflow Async operations]] problem, and use `yield` everywhere you can 🙂.

[[Temporal CLI Cancel Workflow]]