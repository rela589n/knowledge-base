**[[Activity]] Heartbeat**  is a ping that is sent to [[Server|Temporal Service]] so that it can understand that the [[Activity]] is still alive.

Heartbeat can include payload, so that if current [[Worker Process]] fails, a new [[Worker]] may take over the computation from the last saved place. 

[[Samples]] have an example of [[Activity Heartbeat]].

