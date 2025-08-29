---
aliases:
  - Task Timeout
---
**[[Workflow Task]] Timeout** - timeout for one particular [[Workflow Task]] to execute before it's considered failed and is taken to another [[Worker]]. Default is **10 seconds**.

The main reason to increase the value is when workflow has an extensive [[Event History]], and it takes a long time to [[Workflow Replay|Replay]].
