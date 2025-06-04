---
aliases:
  - Schedule Spec
---
Specification of [[Workflow Schedule]] that describes *when* [[Workflow Schedule Action]] should be executed.

Configuration:
- [[Cron Expression]] to specify execution interval;
- [[Workfow Schedule Interval Spec|Interval Spec]] - using code;
- **time bounds** - ensures that [[Workflow Schedule Action|Action]] is not executed before start or after end time;
- [[Jitter]] - random offset of time added to the time;
- Time-Zone - can be set, but it's recommended to use UTC.


