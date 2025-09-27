---
aliases:
  - Aspect
---
[[Bounded Context]] is made up of all the **aspects** *of* the **system** that are **driven *by* the [[Domain Model|Model]]**:
- objects;
- schemas;
- applications.

What's in and what's out of the [[Bounded Context]] is determined by whether it's **driven by the [[Domain Model|Model]]**:
- [[Translation Layer]] is outside of the [[Bounded Context|Context]] (not driven);
- Database Schemas are inside the [[Bounded Context|Context]], (it's driven by the [[Domain Model|Model]]).
