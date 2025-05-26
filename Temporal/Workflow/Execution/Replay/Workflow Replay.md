[[Temporal/Workflow/Workflow Definition|Workflow Definition]]  must be deterministic to ensure **consistent replay** ([[Event Sourcing]]). If you need some randomness (like current time), you should be using `Workflow::sideEffect()`.

**Changes to code** can introduce [[Event History]] problems (if we add some step in between, or change the order, when there's running [[Workflow Execution]]), which is solved with [[Workflow Versioning]].

In case of inconsistent [[Event History]], Temporal will retry the workflow again and again until you finally do something about it.
