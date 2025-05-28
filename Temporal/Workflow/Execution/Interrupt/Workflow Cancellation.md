---
aliases:
  - Cancel a Workflow
---
[[Temporal/Workflow/Workflow|Workflow]] Cancellation is a graceful shutdown of [[Workflow Execution]].

When you cancel the workflow, an `CanceledFailure` exception is thrown, so that if [[Temporal/Workflow/Workflow|Workflow]] defines [[SAGA|compensations]], they'll be executed.
