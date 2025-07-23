---
aliases:
  - Bounded Context Boundaries
  - Boundary
---
To determine **[[Bounded Context]] Boundaries**, you have to understand that the **team is primarily interested** in the **part of the system they'll have to change**, and secondarily in [[Context Integration Map|Integrations]].

**One team** can work on **one (or more) [[Bounded Context|Bounded Contexts]]**, and it's hard to make more than one team to work on a single [[Bounded Context]].

With **big [[Bounded Context]]**:
- Features flow is easier (less [[Context Integration Map|Integration]] overhead);
- [[Continuous Integration]] is harder.

With **small [[Bounded Context]]**:
- [[Continuous Integration]] is easier;
- [[Context Integration Map|Integration]]-Features are harder.

**[[Context Integration Map|Integration]]** only makes sense when there're **small intersections** between [[Bounded Context|Contexts]]. 

It is only present when two **[[Domain Model|Models]] are closely related**, and can be expressed in [[Domain Concept|Terms]] of one another.

**Deep [[Context Integration Map|Integration]]** between [[Bounded Context|Bounded Contexts]] **is impractical**.
It only signifies that two **[[Bounded Context|Contexts]] should've been one**.

> Beware that **you can have a biased opinion** toward the [[Bounded Context|Context]] you're working in.

External subsystems might encompass multiple [[Bounded Context|Bounded Contexts]] as well (not just single one).
