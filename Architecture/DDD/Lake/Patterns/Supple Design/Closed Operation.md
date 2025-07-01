---
aliases:
  - Closure of Operations
---
**Closed Operation** is the operation whose result type is the same as the input type. 

If operation's result is defined by the state of implementer (e.g. implementer's state is the argument of an operation), then return type should be the same type as the implementer.

It's like in mathematics where two real numbers add up only to a new real number, not to something else.

The same goes for [[Value Object|Value Objects]]. Operations should return the same concept, not a new dependency.

The operation should not add extraneous concepts that are not relevant to the problem of the operation.


