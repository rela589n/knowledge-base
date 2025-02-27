---
aliases:
  - Infrastructure-driven packaging
---
Compared to Modularity, folder by type introduces problems:
- every package consists of the components of low [[Cohesion]] (everything is unrelated);
- packages have high [[Coupling]] between themselves (every feature is scattered across multiple inter-dependent packages);
- cognitive load increases as the project increases;
- such partitioning doesn't reveal the underlying model;
- the reasoning about one [[Cohesion|cohesive]] concept requires us to remember multiple technical concepts, keeping them in mind (instead of just being displayed in the project file explorer)

Partitioning should be based on meaning of the objects rather than their types. A good choice is to provide [[Aggregate]] with it's own namespace, and everything related to that [[Aggregate]] should be placed inside.

See DDD Book (MODULES in the Shipping Model).
