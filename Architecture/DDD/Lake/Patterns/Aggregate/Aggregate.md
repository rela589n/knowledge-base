---
aliases:
  - Aggregates
---
Aggregate is a **cluster of related objects**, which make up a logical unit, that allows us to **maintain [[Invariant|business invariants]]** inside of the [[Transaction]]. 

One of them is the [[Aggregate Root|Root]], and others are subordinate objects ([[Entity|Entities]] and [[Value Object|Value Objects]]).

Aggregates are limited within a [[Aggregate Boundary|Boundary]].

- When **we run the [[Transition]]** that touches any object within [[Aggregate Boundary]], all the **[[Invariant|Invariants]] of the [[Aggregate]] must be kept** ([[Aggregate Root]] is responsible for that)
- When we **delete [[Aggregate]]**, we delete everything within [[Aggregate Boundary]];
- When we **clone [[Aggregate]]** (see [[Prototype]]), we should clone only within [[Aggregate Boundary]].
- [[Aggregate resolves the Contention points]]

[[One to Many relationship access is controlled with the Aggregate]]