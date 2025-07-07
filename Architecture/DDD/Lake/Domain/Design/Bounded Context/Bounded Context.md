---
aliases:
  - Bounded Contexts
  - Context
---
**Bounded Context** demarcates a **range of applicability (context) of each [[Domain Model]]**. It is used to **delimit distinctive subsystems** having **its own [[Ubiquitous Language]]**, that can be developed by different teams / departments.

Context of the [[Domain Model|Model]] is a set of conditions under which [[Domain Concept|Model Terms]] have specific meaning.

Total [[Model Unification|Unification]] of the [[Domain Model]] in a large system isn't effective. Most optimal is when [[Bounded Context|Bounded Contexts]] to expose their own small [[Domain Model|Models]] rather than one big over-arching [[Domain Model|Model]].

You should keep [[Domain Model|Model]] strictly [[Model Unification|Unified]] within [[Bounded Context|Context]] and not be distracted with the issues outside.

What's in and what's out of [[Bounded Context|Context]] is determined by whether it's driven by the [[Domain Model|Model]]:
- [[Anti-Corruption Layer|Translation Layer]] is outside of the [[Bounded Context|Context]] (not driven);
- Database Schemas is within the [[Bounded Context|Context]], (it's driven by the [[Domain Model|Model]]).

[[Bounded Context]] is made up of **all the aspects of the system that are driven by the [[Domain Model|Model]]**:
- objects;
- schemas;
- applications.

[[Context Map]] gives big picture of [[Bounded Context|Contexts]] and connections.

**Continuous Integration** keeps the [[Model Unification|Model Unified]] within the [[Bounded Context]].
