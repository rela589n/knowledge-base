---
aliases:
  - Heartbeat Throttling
---
[[Activity Heartbeat|Heartbeat]] messages are throttled when [[Worker]] knows that the heartbeat isn't required to prevent [[Activity Heartbeat Timeout|Heartbeat Timeout]]. Yet, in case of an [[Activity Execution Failure]], the last Heartbeat is reported to the [[Temporal Server|Service]] so that next [[Worker]] will have the most recent progress information.

Beware of this when dealing with [[Activity Cancellation]], since it's only when the request was actually sent to [[Temporal Server|Service]] you can know that [[Activity]] was cancelled.

Presumably, [[Activity Heartbeat Timeout|Heartbeat Timeout]] is also compared with other [[Activity Execution Timeouts]] to prevent throttling when the time is already over. For example, if [[Start-To-Close]] timeout is defined, [[Activity Heartbeat|Heartbeat]] message will be sent right when it's over.
