---
aliases:
  - Bounded Contexts
  - Context
---
**Bounded Context** demarcates a **range of applicability (context) of specific [[Domain Model]]**. It is used to **delimit distinctive subsystems** having **its own [[Ubiquitous Language]]**, that can be developed by different teams / departments.

Context of the [[Domain Model|Model]] is a set of conditions under which [[Domain Concept|Model Terms]] have specific meaning.

You should keep [[Domain Model|Model]] strictly [[Model Unification|Unified]] within [[Bounded Context|Context]] and not be distracted with the issues outside.

Total [[Model Unification|Unification]] of the [[Domain Model]] in a large system isn't effective. Most optimal is to have few [[Bounded Context|Bounded Contexts]] to expose their own small [[Domain Model|Models]] rather than one big over-arching [[Domain Model|Model]].

[[Bounded Context Aspects]] - what's in and what's out.

[[Context Integration Map]] gives big picture of [[Bounded Context|Contexts]] and connections.

