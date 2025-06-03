When throw `\Error` from the workflow, it's retried ([[Workflow Task Failure]]).

[[Workflow Execution]] fails, and it's **not [[Retry Policy|Retried]]** when:
- `TemporalFailure` (like `ApplicationFailure`) is thrown, or when it's raised from the failed [[Activity]];
- calling unknown [[Activity]] method;
- throwing exception.

Status is changed into "Failed" and no more progress is made.