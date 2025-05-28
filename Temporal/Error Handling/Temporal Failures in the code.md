[[SDK]] provides base `TemporalFailure` exception class. It is serialized to [[Protobuf]] and transmitted over network.

[[Activity]]-originated exceptions, raised in the [[Temporal/Workflow/Workflow|Workflow]] are represented as `ActivityFailure`.

The previous exception of `ActivityFailure` represents the cause of the failure:
- `TimeoutFailure` - if timed-out;
- `CanceledFailure` - if [[Activity Cancellation|activity was cancelled]];
- `ApplicationFailure` - the [[Activity|activity]] has thrown (this is [[Application Failure]]).

Throwing `ApplicationFailure` from the [[Workflow Execution|workflow]] causes it to fail. That's the only exception you should throw manually.

Other failures:
- `TerminatedFailure` - when [[Workflow Termination|terminated]];
- `ServerFailure` - exception related to [[Server|Temporal Service]] problems;
- `ChildWorkflowFailure`

Before throwing an exception, temporal runs [[Failure Converter]].
