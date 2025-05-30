---
aliases:
  - Activity Timeout
---
[Documentation](https://docs.temporal.io/encyclopedia/detecting-activity-failures)

> When setting the timeout, it's good practice to set it greater than the maximum time you anticipate the task will require to complete.

It's better to configure timeout than [[Retry Policy]].

Configuring either [[Schedule-To-Close]] or [[Start-To-Close]] is **mandatory** to prevent [[Activity|Activities]] from executing indefinitely.

Timeouts:
- [[Schedule-To-Start]]
- [[Start-To-Close]] 
- [[Schedule-To-Close]]



**[[Activity Heartbeat|HeartBeat]] Timeout** - timeout within which activity must respond with ping before it's considered stuck. Used for long-running activities.
