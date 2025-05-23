[Documentation](https://docs.temporal.io/encyclopedia/detecting-activity-failures)

**Schedule-To-Start** - how long for the [[Activity Task]] is allowed to be [[Activity Task Queue|queued up]] w/o being taken by any of the workers.

**Start-To-Close** (recommended) - timeout for a single execution;

**Schedule-To-Close** timeout is the complete timeout that includes activity retries.

**[[Activity Heartbeat|HeartBeat]] Timeout** - timeout within which activity must respond with ping before it's considered stuck. Used for long-running activities.
