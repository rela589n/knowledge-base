When [[Workflow Task]] fails due to:
- exceptions in the [[Workflow Execution|Workflow]];
- [[Workflow Replay|Non-Deterministic Errors]];
- unknown [[Activity]] method;

Some of these can happen during deployment.

[[Workflow Task Failure|Workflow Task Failures]] are considered [[Transient Failure|transient]], so that devs can fix the code without losing the state of [[Workflow Execution]].

[[Retry Policy|Retry]] include scheduling new [[Workflow Task]], and clearing [[Sticky Workflow Execution]] cache on the [[Worker]].
