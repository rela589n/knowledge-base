---
aliases:
  - Heartbeat Timeout
---
**[[Activity Heartbeat]] Timeout** - timeout within which [[Activity]] must respond with ping before it's worker is considered stuck and activity re-published. Used for long-running activities.

The main idea of [[Activity Heartbeat Timeout|Heartbeat Timeout]] is to prevent a great pity (e.g. time loss) when [[Worker Process]] for a long-running task (say video processing that takes 10 hours) crashes just right after the start, and [[Temporal/Temporal Server|Temporal Server]] knows nothing about it until it reaches the timeout of 12 hours. Even though [[Worker Process]] might have been recovered long ago, [[Activity Task]] isn't available for any [[Worker]] until it times-out, since crashed worker didn't report to [[Temporal/Temporal Server|Temporal Service]].

> You can try running `docker container kill` to kill the container, and find that [[Activity Heartbeat Timeout|Heartbeat Timeout]] is reported in [[Temporal UI|UI]].

Note that code in `catch` block that covers clean-up in case of [[Activity Cancellation]] is subject to [[Activity Heartbeat Timeout|Heartbeat Timeout]] as well. If it does not complete in the expected time, [[Activity]] will end with `"activity Heartbeat timeout"` error.
