**[[Activity]] Heartbeat**  is a ping that is sent to [[Server|Temporal Service]] so that it can understand that the [[Activity]] is still alive and refresh [[Activity Heartbeat Timeout|Heartbeat Timeout]].

> Every [[Activity]] that doesn't complete immediately should heartbeat and set [[Activity Heartbeat Timeout|Heartbeat Timeout]].

Heartbeat can include payload, so that in case [[Worker Process]] fails, a new [[Worker]] will take the computation over from the last saved place. 

Besides other, if the [[Activity]] was [[Activity Timeouts|Timed-out]] or [[Activity Cancellation|Cancelled]],  heartbeat will fail with exception.

[[Samples]] have an example of [[Activity Heartbeat]].
