Categories of failures:
- [[Application Failure]]
- [[Platform Failure]]

Types of failures:
- [[Transient Failure]]
- [[Intermittent Failure]]
- [[Permanent Failure]]

[[Error Propagation]]

[[Activities are Re-Executed]]

Failures in the code

[[SDK]] provides base `TemporalFailure` exception class. It is serialized to [[Protobuf]] and transmitted over network.

[[Activity]]-originated exceptions, raised in the [[Temporal/Workflow/Workflow|Workflow]] are represented as `ActivityFailure`.

The previous exception of `ActivityFailure` represents the cause of the failure:
- `TimeoutFailure` - if timed-out;
- `CanceledFailure` - if [[Activity Cancellation|activity was cancelled]];
- `ApplicationFailure` - the [[Activity|activity]] has thrown (this is [[Application Failure]]).

Throwing `ApplicationFailure` from the [[Workflow Execution|workflow]] causes it to fail. That's the only exception you can throw manually.

