---
aliases:
  - Temporal Failure
---
[[Temporal SDK]] provides base `TemporalFailure` exception class. It is serialized into [[Protobuf]] message and transmitted over network.

[[Activity]]-originated exceptions, raised in the [[Temporal/Workflow/Workflow|Workflow]] are represented as `ActivityFailure`.

The previous exception of `ActivityFailure` contains the details about the failure:
- `TimeoutFailure` - if timed-out;
- `CanceledFailure` - if [[Activity Cancellation|Activity was cancelled]];
- `ApplicationFailure` - if [[Activity|Activity]] has thrown (an [[Application Failure]]).

Throwing `ApplicationFailure` from the [[Workflow Execution|workflow]] causes it to [[Workflow Execution Failure|fail]]. That's the only exception you should throw manually.

Other failures:
- `TerminatedFailure` - when [[Workflow Termination|Workflow was Terminated]];
- `CanceledFailure` - when [[Workflow Cancellation|Workflow was Cancelled]]
- `ServerFailure` - exception related to [[Temporal/Temporal Server|Temporal Service]] problems;
- `ChildWorkflowFailure`

Before throwing an exception, temporal runs [[Failure Converter]].