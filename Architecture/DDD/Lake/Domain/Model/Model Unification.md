---
aliases:
  - DDD Elephant
---
**[[Domain Model|Model]] Unification** - making [[Domain Model|Model]] internally [[Consistency|Consistent]].

Whether to keep [[Bounded Context|Bounded Contexts]] unified or separate should depend on pros and cons of both.

When unifying [[Bounded Context|Bounded Contexts]], there could be the problem that **the same [[Domain Concept|Concept]]** in different [[Bounded Context|Contexts]] may be **represented from the different angles** (like [[#^4c61c2|elephant]]). 
Some things are unique, but some things represent the same [[Domain Concept|Thing]] (snake vs fire hose, tusk vs stick).

If there's no enough knowledge about the [[Domain Concept|Conceptual]] makeup of the [[Domain Model|Model]], it can be gained by [[Model Refinement|Refinements]], leading to [[Model Breakthrough]].

Blind men have to recognize the **incompleteness of their perception** of the elephant:
![[Elephant View.png]] ^4c61c2