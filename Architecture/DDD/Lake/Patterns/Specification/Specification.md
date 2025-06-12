---
developed-by:
  - Evans
  - Fowler
origin: Applying and Implementing SPECIFICATION
---
> Some [[Domain|Business]] rules (those including lots of conditions) could not find their place in any [[Entity]] or [[Value Object]]. They deserve a designated [[Specification]] object.

**Specification** is a [[Predicate]]-like object that **defines a Criteria**, and encapsulates the algorithms of verifying whether the object satisfies that Criteria. More generally, it defines **"what it means to be `<adjective>`"**, and it can evaluate it for candidate.

[[Specification]] allows the client to **specify "what" he wants** (in terms of [[Ubiquitous Language|Language]]) not being concerned with "how".

[[Specification]] is suitable for these use-cases:
- [[Specification for Validation|Validation]];
- [[Specification for Selection|Selection]];
- [[Specification for Building to order|Building to order]].

The main aim of the [[Specification]] is the **conceptual unity** of the three.

> If [[Specification]] needs some external things to check the condition, [[Factory]] could be used to create it.

**Examples** of [[Specification]]:
- [[Doctrine Criteria]];
- Filters (method `apply()`).
