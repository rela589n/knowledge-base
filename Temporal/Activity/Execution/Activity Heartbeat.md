**[[Activity]] Heartbeat**  is a ping that is sent to [[Server|Temporal Service]] so that it can understand that the [[Activity]] is still alive.

The main idea of heartbeat is to prevent a great pity (e.g. time loss) when [[Worker Process]] for a long-running task (say video processing that takes 10 hours) crashes just right after start, and [[Server|Temporal Server]] knows nothing about it until it reaches the timeout is 12 hours. Even though [[Worker Process]] might have been recovered long ago, [[Activity Task]] isn't available for anybody, since crashed worker didn't respond to [[Server|Temporal Service]].

Heartbeat can include payload, so that in case [[Worker Process]] fails, a new [[Worker]] will take the computation over from the last saved place. 

Besides other, if the [[Activity]] was [[Activity Timeouts|Timed-out]] or [[Activity Cancellation|Cancelled]],  heartbeat will fail with exception.

[[Samples]] have an example of [[Activity Heartbeat]].
