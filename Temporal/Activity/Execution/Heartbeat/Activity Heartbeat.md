**[[Activity]] Heartbeat**  is a ping that is sent to [[Temporal Server|Temporal Service]] so that it can understand that the [[Activity]] is still alive and refresh [[Activity Heartbeat Timeout|Heartbeat Timeout]].

> Every [[Activity]] that doesn't complete immediately should heartbeat and set [[Activity Heartbeat Timeout|Heartbeat Timeout]].

Heartbeat can include payload, so that in case [[Worker Process]] fails, a new [[Worker]] will take the computation over from the last saved place. 

Besides other, if the [[Activity]] was [[Activity Timeouts|Timed-out]] or [[Activity Cancellation|Cancelled]],  heartbeat will throw an exception (even though [[Activity Heartbeat Timeout|Heartbeat Timeout]] might not be specified). ^e33915

Heartbeat messages are throttled when [[Worker]] knows that the heartbeat isn't required to prevent [[Activity Heartbeat Timeout|Heartbeat Timeout]]. Yet, in case of an [[Activity Execution Failure]], the last Heartbeat is reported to the [[Temporal Server|Service]] so that next [[Worker]] will have last progress information.

[[Samples]] have an example of [[Activity Heartbeat]].
