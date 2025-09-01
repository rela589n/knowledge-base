---
aliases:
  - DIP
  - Inversion of dependency
  - Dependency Inversion
---
**Dependency Inversion** calls for **depending on abstractions** rather than concretions. 

**If** at some point  we would **need to** change/**complement the implementation** (e.g. add [[Decorator]], [[Proxy]]), it'd be easier. 

[[Dependency inversion principle|Dependency Inversion]] inverts [[Coupling]] (dependency) direction, reducing the [[Coupling]] on one side, but increasing it on the other. ^46641c