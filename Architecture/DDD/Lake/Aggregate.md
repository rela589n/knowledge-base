This is the [[Aggregate Root|object]] that represents a cluster of child objects, responsible of maintaining the [[Invariant|invariants]] within some [[Aggregate Boundary|boundary]] during the changes.

- When we commit any transaction, all the [[Invariant|invariants]] of the [[Aggregate Boundary|aggregate objects]] must be satisfied ([[Aggregate Root]] is responsible for that)
- When we delete aggregate, we just delete everything within [[Aggregate Boundary]]
