With the usage of [[Aggregate|Aggregates]], [[Contention]] points should become looser, and important business [[Invariant|Invariants]] should become tighter.

This is due to the fact that [[Invariant|Invariants]] that span multiple [[Aggregate|Aggregates]] aren't expected to be met all the time.

For example, price of the product can be updated at any stage of the order.

![[Aggregate invariant.png]]

If it's updated during order progress, it would violate [[Invariant]]. 

Price must become part of PO [[Aggregate]], and the [[Invariant]] will be kept.

Not all existing orders should reflect the real price. 
At least, archived orders should be kept with the purchase price, not with the latest one.

For active orders we could present customer with the fact that item price is outdated and make him do the adjustments.
