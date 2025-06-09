---
aliases:
  - Infrastructure-driven packaging
  - Tier-based packaging
---
Compared to [[Module|Modularity]], objects that conceptually have very little relationship are crammed together:
- every package consists of the components of low [[Cohesion]] (everything is unrelated, business-wise);
- packages have high [[Coupling]] between themselves (every feature is scattered across multiple inter-dependent packages);
- cognitive load increases as the project increases;
- such partitioning doesn't reveal the [[Domain Model|Model]];
- the reasoning about one [[Cohesion|Cohesive]] concept (like features of [[Aggregate]]) require us to remember multiple technical concepts, scattered a keeping them in mind (instead of just being displayed in the project file explorer)

Partitioning should be based on meaning of the objects rather than their types. A good choice is to provide [[Aggregate]] with it's own namespace, and everything related to that [[Aggregate]] should be placed inside.

See DDD Book (MODULES in the Shipping Model).


