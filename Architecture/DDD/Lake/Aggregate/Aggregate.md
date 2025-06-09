Aggregate is a **cluster of related objects**, which make up a logical unit, that allows us to **maintain [[Invariant|business invariants]]** inside of the [[Transactions]]. 

One of them is the [[Aggregate Root|Root]], and others are subordinate objects ([[Entity|Entities]] and [[Value Object|Value Objects]]).

Aggregates are limited within a [[Aggregate Boundary|Boundary]].

- When **we run the [[Transition]]** that touches any object within [[Aggregate Boundary]], all the **[[Invariant|Invariants]] of the [[Aggregate]] must be kept** ([[Aggregate Root]] is responsible for that)
- When we **delete [[Aggregate]]**, we delete everything within [[Aggregate Boundary]];
- When we **clone [[Aggregate]]** (see [[Prototype]]), we should clone only within [[Aggregate Boundary]].

[[Invariant|Invariants]] that span multiple [[Aggregate|Aggregates]] aren't expected to be met all the time.

High [[Contention]] points should become looser, and important business [[Invariant|Invariants]] should become tighter.

For example, price of the part could be updated at any stage of the order. Yet, it should not always reflect the existing orders.

![[Aggregate invariant.png]]



At least, archived orders should be kept with the purchase price, not with the latest one.

For active orders we could present customer with the fact that item price is outdated and make him do the adjustments.
