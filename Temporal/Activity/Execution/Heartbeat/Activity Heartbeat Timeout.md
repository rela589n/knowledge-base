---
aliases:
  - Heartbeat Timeout
---
**[[Activity Heartbeat]] Timeout** - timeout within which [[Activity]] must respond with ping before it's considered stuck. Used for long-running activities.

The main idea of [[Activity Heartbeat Timeout|Heartbeat Timeout]] is to prevent a great pity (e.g. time loss) when [[Worker Process]] for a long-running task (say video processing that takes 10 hours) crashes just right after start, and [[Server|Temporal Server]] knows nothing about it until it reaches the timeout is 12 hours. Even though [[Worker Process]] might have been recovered long ago, [[Activity Task]] isn't available for anybody, since crashed worker didn't respond to [[Server|Temporal Service]].