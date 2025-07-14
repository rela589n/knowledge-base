To determine **[[Bounded Context]] Boundaries**, you have to understand that the **team is primarily interested** in the **part of the system they'll have to change**, and secondarily in [[Context Integration Map|Integrations]].

**One team** can work on **one (or more) [[Bounded Context|Bounded Contexts]]**, and it's hard to make more than one team to work on a single [[Bounded Context]].

> Understand that **you can have biased opinion** due to the [[Bounded Context|Context]] you're working in.

Deep [[Context Integration Map|Integration]] between [[Bounded Context|Bounded Contexts]] is impractical.

With big [[Bounded Context]]:
- Features flow is easier (less [[Context Integration Map|Integration]] overhead);
- [[Continuous Integration]] will have some overhead.

With small [[Bounded Context]]:
- [[Continuous Integration]] is easier;
- Features flow is harder ([[Context Integration Map|Integration]]).

External subsystems might be represented as multiple [[Bounded Context|Bounded Contexts]] as well.
