---
aliases:
  - Model Unification
  - Unified
  - Valid within
  - Elephant
  - Consistent
---
**[[Domain Model|Model]] Consistency** - imperative property of the [[Domain Model|Model]] not to have [[Model Contradictions|Contradictions]]:
- **[[Invariant|Invariants]] are kept**;
- **[[Domain Concept|Terms]] are unambiguous**;
- **[[Business Rule|Rules]] do not contradict**.

It's the most fundamental requirement of the [[Domain Model|Model]] that makes it usable.

**[[Domain Model|Model]] Unification** - making [[Domain Model|Model]] internally [[Consistency|Consistent]].

Whether to keep [[Bounded Context|Bounded Contexts]] unified or separate should depend on pros and cons of both.

When [[Model Consistency|Unifying]] [[Bounded Context|Bounded Contexts]], it's the problem that in different [[Bounded Context|Contexts]] the same [[Domain Concept|Concept]] may be **represented from a different angles** (like [[#^4c61c2|elephant]]). Some things are unique, but some things represent the same [[Domain Concept|Thing]] (snake vs fire hose).

If there's no enough knowledge about the [[Domain Concept|Conceptual]] makeup of the [[Domain Model|Model]], it can be gained by [[Model Refinement|Refinements]], leading to [[Model Breakthrough]].

Blind men have to recognize the **incompleteness of their perception** of the elephant:
![[Elephant View.png]] ^4c61c2