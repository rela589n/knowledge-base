---
aliases:
  - Model Consistency
  - Unified
  - Valid within
---
The most fundamental requirement of [[Domain Model|Model]] is that it **be internally consistent** (no contradictions). *Unification* - [[Invariant|Invariants]] are kept, terms are unambiguous, rules do not contradict.

When [[Model Unification|Unifying]] [[Bounded Context|Bounded Contexts]], it's the problem that in different [[Bounded Context|Contexts]] the same [[Domain Concept|Concept]] may be **represented from a different angles** (like **elephant**). Something is unique, but something is a different representation of the same [[Domain Concept|Thing]].

If there's no enough knowledge about the [[Domain Concept|Conceptual]] makeup of the [[Domain Model|Model]], it can be gained by [[Model Refinement|Refinements]], leading to [[Model Breakthrough]].

Blind men have to recognize the **incompleteness of their perception**:
![[Elephant View.png]]