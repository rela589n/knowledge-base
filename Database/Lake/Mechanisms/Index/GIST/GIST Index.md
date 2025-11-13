---
docs:
  - https://habr.com/ru/companies/postgrespro/articles/444742/
---
**Generalized Search Tree [[Database Index|Index]]** *allows to* ***distribute* complex data** (like [[Point]]) ***across* [[Balanced Tree]]** 
*using* rules.

Answer **queries** *of* **relative position** operators:
- *located to* the left / *to* the right;
- *contains*;
- *overlaps*.

It ***organizes* data** *using* **summaries** ([[Predicate]]):
- folder nodes (from root):
	- [[Predicate]];
	- references to child nodes;
- leaf nodes:
	- contain [[Predicate]];
	- pointer to data that meets this [[Predicate]].

[[Predicate]] of parent node 
comprises all [[Predicate]]s of child nodes.

See:
- [[R-Tree]]

>**Internals**
>can be [inspected with](https://habr.com/ru/companies/postgrespro/articles/444742/) `gevel` ext.
