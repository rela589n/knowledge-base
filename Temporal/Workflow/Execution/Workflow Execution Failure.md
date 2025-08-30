When `\Error` is thrown from the workflow, it results in [[Workflow Task Failure]] that's retried .

[[Workflow Execution]] fails **without being [[Retry Policy|Retried]]** when:
- `TemporalFailure` (like `ApplicationFailure`) is thrown, or when it's raised from the failed [[Activity]];
- calling unknown [[Activity]] method;
- throwing exception.

Status is changed into "Failed" and no more progress is made.