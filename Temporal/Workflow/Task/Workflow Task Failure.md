[[Workflow Task]] fails due to anything but `TemporalFailure`:
- Errors in the [[Workflow Execution|Workflow]] (`\Error` - division by zero, type errs);
- [[Workflow Replay|Non-Deterministic Errors]];

Some of these can happen during deployment.

[[Workflow Task Failure|Workflow Task Failures]] are considered [[Transient Failure|transient]], so that devs can fix the code without losing the state of [[Workflow Execution]].

[[Retry Policy|Retry]] anticipates scheduling new [[Workflow Task]], and clearing [[Sticky Workflow Execution]] cache off the [[Worker]].

Other errors cause [[Workflow Execution Failure]]

