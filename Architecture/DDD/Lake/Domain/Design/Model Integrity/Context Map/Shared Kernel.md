**Shared Kernel** is highly **cooperative [[Context Integration Strategies|Relationship]]** in which two **[[Bounded Context|Bounded Contexts]]** *have* some **parts of the [[Code]]** (and other [[Bounded Context Aspects|Aspects]]) **physically shared**.

Useful when it's too **much overhead** *for* **full [[Unified Model|Unification]]** of the [[Domain Model|Models]]. We can **synchronize** *only* the **subset** *of* **[[Domain Model|Model]] citizens**.

We only **reduce duplication**, but **not eliminate it** completely compared to how it would've been in case of one [[Bounded Context]].

The **changes** to the **shared stuff** must only be introduced by **consulting** the **other team**. Both team's tests must pass.

*If* team's **[[Continuous Integration|Sync]] rate** is *once* **a day**,
*then* [[Shared Kernel]] **[[Continuous Integration|Integration]] rate** could be *once* **a week**.

Often [[Shared Kernel]] is [[Core Domain]], some set of [[Generic Subdomain]].

[[Shared Kernel]] imposes **burden *on* Deployment** 
as much as ***on* development**.

