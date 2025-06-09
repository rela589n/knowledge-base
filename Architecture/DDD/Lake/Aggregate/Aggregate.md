Aggregate is a [[Aggregate Boundary|Bounded]] **cluster of objects** with one of them being the [[Aggregate Root|Root]], and multiple subordinate objects ([[Entity|Entities]] and [[Value Object|Value Objects]]), allowing us to maintain [[Invariant|business invariants]] during the changes:

- When **we run the transaction**, all the [[Invariant|Invariants]] of the [[Aggregate]] must be kept ([[Aggregate Root]] is responsible for that)
- When we **delete [[Aggregate]]**, we delete everything within [[Aggregate Boundary]];
- When we **clone [[Aggregate]]**, we clone everything within [[Aggregate Boundary]].

High contention points should become looser, while important business invariants should become tighter.

![[Aggregate invariant.png]]

Price of the part could be updated at any stage of the order. 

Yet, it should not always reflect the existing orders.

At least, archived orders should be kept with the purchase price, not with the latest one.

For active orders we could present customer with the fact that item price is outdated and make him do the adjustments.
