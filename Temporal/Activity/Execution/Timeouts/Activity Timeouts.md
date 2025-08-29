---
aliases:
  - Activity Timeout
docs:
  - https://docs.temporal.io/encyclopedia/detecting-activity-failures
---
**Timeouts** are crucial in the case like [[Worker]] failure. If [[Worker]] fails and isn't recovered, no activities will be executed, and nobody will know that anything has gone wrong.

It's good practice to set it **greater than the maximum time** you anticipate the task to complete.

Timeouts:
- [[Schedule-To-Start]] (before execution, *optional*)
- [[Activity Execution Timeouts|Execution Timeouts]] (*mandatory*)


To handle [[Rate Limiting]], you can configure [[Exponential backoff|backoff coefficient]] respectively. Usually having this by itself will mean that you won't have [[Schedule-To-Close]] timeout, so you'd use [[Schedule-To-Start]] and [[Start-To-Close]] timeouts, and [[Retry Policy]].

[[Activity Heartbeat Timeout]]
