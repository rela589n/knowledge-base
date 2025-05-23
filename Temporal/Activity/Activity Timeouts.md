[Documentation](https://docs.temporal.io/encyclopedia/detecting-activity-failures)

**Schedule-To-Start** - how much time is [[Activity Task]] is allowed to be in [[Activity Task Queue|queue]] w/o being taken by any of the workers.

**Start-To-Close** (recommended) - single execution;

**Schedule-To-Close** = Schedule-To-Start + Start-To-Close.

**HeartBeat** - for long-running activities, the limit of time within which activity must send before it's considered stuck.

