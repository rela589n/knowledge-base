This is the [[Aggregate Boundary|limited]] cluster of objects with one object being the [[Aggregate Root|root]], and multiple subordinate objects, allowing us to maintain [[Invariant|business invariants]] during the changes:

- When we commit any transaction, all the [[Invariant|invariants]] of the [[Aggregate]] must be satisfied ([[Aggregate Root]] is responsible for that)
- When we delete aggregate, we must delete everything within [[Aggregate Boundary]]

High contention points should become looser, while important business invariants should become tighter.

![[Aggregate invariant.png]]

Price of the part could be updated at any stage of the order. 

Yet, it should not always reflect the existing orders.

At least, archived orders should be kept with the purchase price, not with the latest one.

For active orders we could present customer with the fact that item price is outdated and make him do the adjustments.
