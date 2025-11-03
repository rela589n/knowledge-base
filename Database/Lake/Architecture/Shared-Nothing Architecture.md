**Shared-Nothing Architecture** - each node has **it's own resources**, which are not shared. 

It *adds* **application complexity**, which the database can no longer hide.

**Communication *between* nodes** is with app [[Code]] ***via* the [[Async Network|Network]]**. No direct disk / memory access. 

It is possible to **distribute data** across multiple regions, thus **reduce latency** for users.

**Shared-nothing** is a **optimal way** to build systems:
- relatively **cheap**;
- requires **no special hardware**;
- **[[Reliability]]** may be achieved **via [[Redundancy]]**.
