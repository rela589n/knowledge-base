---
aliases:
  - Service
---
**Service** is an abstraction over [[POD]] type that offers a **static address**. Even if [[POD]] dies, Service creates a new one.

Services can be:
- **internal** (inaccessible form the outside of the [[Node]]);
- **external** (accessible from outside by **[[Node]]'s IP and port**).

![[K8s.png|300]]