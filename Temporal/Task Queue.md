[[Temporal]] [[Task]] queues are used to queue incoming [[Task|tasks]] before processing. There's an [[Activity Task Queue]] and [[Workflow Task Queue]].

How does it know which task queue to use? You specify it in `WorkflowOptions` and `ActivityOptions` when launching the workflow.
