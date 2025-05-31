**[[Activity]] Heartbeat**  is a ping that is sent to [[Server|Temporal Service]] so that it can understand that the [[Activity]] is still alive.

Heartbeat can include payload, so that in case [[Worker Process]] fails, a new [[Worker]] will take the computation over from the last saved place. 

Besides other, heartbeat will fail if [[Activity]] was timed-out or explicitly cancelled ([[Activity Cancellation]]).

[[Samples]] have an example of [[Activity Heartbeat]].

