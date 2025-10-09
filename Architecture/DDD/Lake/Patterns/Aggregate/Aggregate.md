---
aliases:
  - Aggregates
---
**Aggregate** is a **cluster** of **related objects**, which 
makes up a **logical unit**, that 
allows to **maintain [[Invariant|Invariants]]** inside of the [[Transaction]]. 

- All **[[Aggregate]] [[Invariant|Invariants]] must be kept** 
  in all **[[Transaction]]s** that touch objects within [[Aggregate Boundary]]
  ([[Aggregate Root|Root]] is responsible for it);
- When we **delete [[Aggregate]]**, 
  we delete everything **within [[Aggregate Boundary|Boundary]]**;
- When we **clone [[Aggregate]]** (see [[Prototype]]), 
  we clone only **within [[Aggregate Boundary|Boundary]]**.
- [[Aggregate resolves the Contention points]]

Aggregate consists of:
- [[Aggregate Root|Root]] entity;
- [[Subordinate Objects]]

It is limited by a [[Aggregate Boundary|Boundary]]

[[One to Many relationship access is controlled by the Aggregate]]