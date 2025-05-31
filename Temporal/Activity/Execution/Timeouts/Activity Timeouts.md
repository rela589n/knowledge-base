---
aliases:
  - Activity Timeout
---
[Documentation](https://docs.temporal.io/encyclopedia/detecting-activity-failures)

Timeouts are crucial in the case like [[Worker]] failure. If [[Worker]] fails and isn't recovered, no activities will be executed, and nobody will know that anything has gone wrong.

> When setting the timeout, it's good practice to set it greater than the maximum time you anticipate the task to complete.

It's mandatory to configure either [[Schedule-To-Close]] or [[Start-To-Close]] timeout.

Timeouts:
- [[Schedule-To-Start]]
- [[Execution Timeouts]]

> In almost all cases it's better to configure [[Schedule-To-Close]] timeout than [[Retry Policy]], since usually it's unlikely that next retry has more chance for success.

To handle [[Rate Limiting]], you can configure backoff coefficient respectively. Usually having it will by itself mean that you won't have [[Schedule-To-Close]] timeout, so you'd use [[Schedule-To-Start]] and [[Start-To-Close]] timeouts, and [[Retry Policy]].

**[[Activity Heartbeat|HeartBeat]] Timeout** - timeout within which activity must respond with ping before it's considered stuck. Used for long-running activities.

