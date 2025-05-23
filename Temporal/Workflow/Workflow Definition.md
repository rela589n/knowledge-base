[[Temporal/Workflow/Workflow|Workflow]] Definition is the code that defines the [[Temporal/Workflow/Workflow|Workflow]].

[[Temporal/Workflow/Workflow Definition|Workflow Definition]]  must be deterministic to ensure consistent replay ([[Event Sourcing]]). If you need some randomness, you should be using `Workflow::sideEffect()`.
