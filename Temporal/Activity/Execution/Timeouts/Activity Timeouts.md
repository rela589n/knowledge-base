---
aliases:
  - Activity Timeout
---
[Documentation](https://docs.temporal.io/encyclopedia/detecting-activity-failures)

> When setting the timeout, it's good practice to set it greater than the maximum time you anticipate the task to complete.

It's mandatory to configure either [[Schedule-To-Close]] or [[Start-To-Close]] timeout.

Timeouts:
- [[Schedule-To-Start]]
- [[Start-To-Close]] 
- [[Schedule-To-Close]]

> In almost all cases it's better to configure [[Schedule-To-Close]] timeout than [[Retry Policy]], as it's seldom that next retry has more chance for success.

**[[Activity Heartbeat|HeartBeat]] Timeout** - timeout within which activity must respond with ping before it's considered stuck. Used for long-running activities.
