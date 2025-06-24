---
aliases:
  - Dependency inversion principle
  - Inversion of dependency
  - Dependency Inversion
---
**Dependency Inversion** anticipates that your [[Code]] should depend on abstractions, not on concretions. 

If at some point we could need to change/extend the implementation (e.g. add [[Decorator]], [[Proxy]]), it'd be easier given that we depend on the abstract class/interface. 

[[DIP|Dependency Inversion]] inverts [[Coupling]] (dependency) direction, reducing the [[Coupling]] on one side, but increasing it on the other. ^46641c