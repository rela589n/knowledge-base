---
aliases:
  - Activity Timeout
---
[Documentation](https://docs.temporal.io/encyclopedia/detecting-activity-failures)

> When setting the timeout, it's good practice to set it greater than the maximum time you anticipate the task will require to complete.

Timeouts:
- [[Schedule-To-Start Timeout]]
- [[Start-To-Close Timeout]]
- [[Schedule-To-Close Timeout]]

**[[Activity Heartbeat|HeartBeat]] Timeout** - timeout within which activity must respond with ping before it's considered stuck. Used for long-running activities.
