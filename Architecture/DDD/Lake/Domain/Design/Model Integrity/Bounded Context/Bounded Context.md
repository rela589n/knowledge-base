---
aliases:
  - Bounded Contexts
  - Context
---
**Bounded Context** is a context that demarcates a **range of applicability of specific [[Domain Model]]**. 

It is used to **delimit distinctive subsystems** with **its own [[Ubiquitous Language]]**, that can be developed by different teams / departments.

[[Bounded Context|Context]] **keeps [[Domain Model|Model]] strictly [[Model Consistency|Consistent]]** within its [[Bounded Context Boundary|Boundary]], and must not be distracted with the issues outside.

Total [[Model Consistency|Unification]] of the [[Domain Model|Model]] in a large system isn't effective. Most optimal is to have few [[Bounded Context|Bounded Contexts]] to expose their own small [[Domain Model|Models]] rather than one big over-arching [[Domain Model|Model]]. See [[Bounded Context Boundary|Bounded Context Boundaries]].

Context of the [[Domain Model|Model]] is a set of conditions under which [[Domain Concept|Model Terms]] have specific meaning.

[[Bounded Context Aspects]] - what's in and what's out.

[[Context Integration Map]] gives big picture of [[Bounded Context|Contexts]] and connections.

