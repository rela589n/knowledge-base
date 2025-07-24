---
aliases:
  - Bounded Context Boundaries
  - Boundary
---
**[[Bounded Context]] Boundaries** demarcates the [[Bounded Context|Context]].

The **team is primarily interested** in the part of the system **they'll have to change**, and secondarily in [[Context Integration Map|Integrations]]. Beware that you can have a **biased opinion** toward the [[Bounded Context|Context]] you're working in.

There's a correspondence of **one team per [[Bounded Context]]**.

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
It only signifies that **two [[Bounded Context|Contexts]] should've been one**.

External subsystems might encompass multiple [[Bounded Context|Bounded Contexts]] as well (not just single one).

Note that **[[Bounded Context Boundary|Boundaries]] impact the Deployment**.
