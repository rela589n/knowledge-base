---
aliases:
  - Workflow side effects
  - Workflow time
  - Non-Deterministic Errors
---
[[Temporal/Workflow/Workflow Definition|Workflow Definition]]  must be deterministic to ensure **consistent replay** ([[Event Sourcing]]). If you need some randomness (like current time), you should be using `Workflow::sideEffect()`.

**Changes to code** can introduce Non-Deterministic Errors ([[Event History]] problems) - if we add some step in between, or change the order, when there's running [[Workflow Execution]]. This is solved with [[Workflow Versioning]].

In case of inconsistent [[Event History]], Temporal will retry the workflow again and again until you finally do something about it. Even if [[Workflow Cancellation|Workflow is Cancelled]], you won't be able to run [[SAGA|compensations]] if history is inconsistent.
