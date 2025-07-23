---
aliases:
  - Model Consistency
  - Unified
  - Valid within
  - Elephant
---
**[[Domain Model|Model]] Unification** - the most fundamental requirement of [[Domain Model|Model]] that it must **be internally consistent** (no contradictions). **[[Invariant|Invariants]] are kept**, **[[Domain Concept|Terms]] are unambiguous**, **rules do not contradict**.

Whether to keep [[Bounded Context|Bounded Contexts]] unified or separate should depend on pros and cons of both.

When [[Model Unification|Unifying]] [[Bounded Context|Bounded Contexts]], it's the problem that in different [[Bounded Context|Contexts]] the same [[Domain Concept|Concept]] may be **represented from a different angles** (like [[#^4c61c2|elephant]]). Some things are unique, but some things represent the same [[Domain Concept|Thing]] (snake vs fire hose).

If there's no enough knowledge about the [[Domain Concept|Conceptual]] makeup of the [[Domain Model|Model]], it can be gained by [[Model Refinement|Refinements]], leading to [[Model Breakthrough]].

Blind men have to recognize the **incompleteness of their perception** of the elephant:
![[Elephant View.png]] ^4c61c2