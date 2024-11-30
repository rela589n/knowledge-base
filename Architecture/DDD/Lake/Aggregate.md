This is the object that represents a cluster of related objects responsible of maintaining the [[Invariant|Invariants]] of the child elements during the changes.

Each aggregate has:
- [[Aggregate Root|root]];
- [[Aggregate boundary|boundary ]].

Only [[Aggregate Root]] can be obtained by the database query. Inner objects must be obtained by the traversal of [[Associations]].

> For instance, if we have Car ([[Aggregate Root]]) entity that has four Wheels, there's no point of querying wheel objects from the database and then checking what Car these belong to. Actually, usually it is vice versa - we query database to find Car, and then check the particular wheel of that Car.

When we commit change to any object of the [[Aggregate boundary]], all the [[Invariant|invariants]] must be satisfied.


