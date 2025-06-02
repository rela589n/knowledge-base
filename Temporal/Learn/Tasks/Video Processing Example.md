Implement long-running activity that takes long time to complete.

Configure [[Activity Heartbeat Timeout]] such that in case of worker crash the [[Server]] will detect it w/o waiting for activity timeout to be elapsed, and will re-schedules it.

Use [[Workflow Dependency Injection|Workflow Constructor argument]] to use dynamic [[Start-To-Close]] timeout.

Try to [[Workflow Cancellation|Cancel a Workflow]] and [[Workflow Termination|Kill a Workflow]].
Find out [[Compensation is not executed during Cancellation]] problem, solve it.
Make `cancel()` sleep for time, longer than [[Activity Heartbeat Timeout|Heartbeat Timeout]]. 

