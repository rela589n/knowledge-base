Two [[Bounded Context|Contexts]] were going **[[Separate Ways]]**
- *resulting* in **[[Duplicate Concept|Duplicated Concepts]]**
	- *thereby* **[[Translation Layer|Translation]] *is* hard**
	- *and* **[[Model Refinement|Communication]] *is* vague**

Steps:
- *(preliminaries)*:
	- [[Bounded Context|Context]]'s [[Domain Model|Models]] must be [[Unified Model|Unified]]
	- Set up [[Testing]]
- Choose something **simple** to start
- Work out **shared [[Domain Model|Model]]**
	- identify [[Duplicate Concept|Duplicates]], map them
	- choose way of [[Unified Model|Unification]]:
		- shift toward one, [[Refactoring|Refactor]] the other;
		- choose one [[Domain Concept|Concept]] at a time, and [[Refactoring|Refactor]] the other;
		- build a [[Good Models lie deep|Deep Model]] that'll serve both.
	- Implement the [[Domain Model|Model]]:
- Integrate [[Bounded Context|Contexts]] with new [[Shared Kernel]].
- Remove [[Translation Layer]]

When you meet **[[Dialect Concept|Dialect]]**, it's wise to **postpone** it until [[Model Breakthrough|Breakthrough]].

This refactoring can move into [[Merging Shared Kernel into Single Context]].
