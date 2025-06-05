Implement long-running activity that takes long time to complete.

Configure [[Activity Heartbeat Timeout]] such that in case of worker crash the [[Temporal Server]] will detect it w/o waiting for activity timeout to be elapsed, and will re-schedules it.

Use [[Workflow Constructor Init method|Workflow Constructor argument]] to use dynamic [[Start-To-Close]] timeout.

Try to [[Workflow Cancellation|Cancel a Workflow]] and [[Workflow Termination|Kill a Workflow]].
Find out [[Compensation is not executed during Cancellation]] problem, solve it.

Make `cancel()` sleep for time, longer than [[Activity Heartbeat Timeout|Heartbeat Timeout]] - it will result in timed-out compensation, and it'll be executed again.  It's just an ordinary [[Activity]] that is scheduled.

What will happen, if you catch CancellationException and throw another exception, different from this one? In other words, what happens if your code failed to handle cancellation request?


