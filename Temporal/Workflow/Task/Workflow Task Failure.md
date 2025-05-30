[[Workflow Task]] fails due to:
- Errors in the [[Workflow Execution|Workflow]] (`\Error` - division by zero, type errs);
- [[Workflow Replay|Non-Deterministic Errors]];

Some of these can happen during deployment.

Other errors, including `TemporalFailure` cause [[Workflow Execution Failure]].

[[Workflow Task Failure|Workflow Task Failures]] are considered [[Transient Failure|transient]], so that devs can fix the code without losing the state of [[Workflow Execution]].

[[Workflow Task]] retry anticipates scheduling new [[Workflow Task]], and clearing [[Sticky Workflow Execution]] cache off the [[Worker]].

