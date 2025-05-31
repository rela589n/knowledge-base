**[[Activity]] Heartbeat**  is a ping that is sent to [[Server|Temporal Service]] so that it can understand that the [[Activity]] is still alive.

The main idea of heartbeat is to prevent a great pity when [[Worker]] for a long-running task (say video processing that takes 10 hours) crashes just right after it had started, and [[Server|Temporal Service]] knows nothing about it, and since timeout is 12 hours, it'll faithfully wait for these 12 hours to find out.

Heartbeat can include payload, so that in case [[Worker Process]] fails, a new [[Worker]] will take the computation over from the last saved place. 

Besides other, heartbeat will fail if [[Activity]] was timed-out or cancelled ([[Activity Cancellation]]).

[[Samples]] have an example of [[Activity Heartbeat]].
