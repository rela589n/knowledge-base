---
aliases:
  - Task Queues
---
[[Temporal]] [[Task]] Queues queue up the incoming [[Task|tasks]] before processing. There are [[Activity Task Queue]] and [[Workflow Task Queue]].

Temporal knows which task queue to use by you specifying it in `WorkflowOptions` and `ActivityOptions` when launching the workflow.

Queues allow [[Task Routing]].