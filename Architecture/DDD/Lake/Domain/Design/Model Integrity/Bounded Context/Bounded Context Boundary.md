---
aliases:
  - Bounded Context Boundaries
  - Boundary
---
**[[Bounded Context]] Boundaries** demarcates the [[Bounded Context|Context]].

The **team's primarily interested**
*in* the parts of the system **they'll *have to* work with**,
*and* only then in **[[Context Integration Map|Integrations]] (secondarily)**. 

Beware that you can have a **biased opinion** 
*toward*  the **your [[Bounded Context|Context]]** you're working with.

There's a correspondence of **team *per* [[Bounded Context]]**:

**One team** can work on **one (or more) [[Bounded Context|Bounded Contexts]]**, 
***and*** making **more than one** team to work on a single [[Bounded Context]] ***is* hard**.

With **big [[Bounded Context]]**:
- Features flow is easier (less [[Context Integration Map|Integration]] overhead);
- [[Continuous Integration]] is harder.

With **small [[Bounded Context]]**:
- [[Continuous Integration]] is easier;
- [[Context Integration Map|Integration]]-Features are harder.

**[[Context Integration Map|Integration]]** of [[Bounded Context|Contexts]] only **makes sense** 
*when* **[[Domain Model|Models]]** *are* **closely related** 
*having* **small intersections**,
*so that* one can be **expressed** in [[Domain Concept|Terms]] of another.

**Deep [[Context Integration Map|Integration]]** *is* **impractical**. It only signifies 
that **two [[Bounded Context|Contexts]]** *should've been* **one**.

External subsystems might represent multiple [[Bounded Context|Bounded Contexts]], not just single one.

Note that **[[Bounded Context Boundary|Boundaries]] impact the Deployment**.
