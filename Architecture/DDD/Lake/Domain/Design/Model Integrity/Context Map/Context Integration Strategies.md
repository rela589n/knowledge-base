---
aliases:
  - Context Map Relationship
  - Bounded Context Relationships
  - Integration Strategies
  - Integration Relationships
  - Context Map Strategies
---
**[[Bounded Context|Context]] Integration Strategies** are Patterns that define the nature of the **relationships *between* [[Bounded Context|Contexts]]**.

They depend mostly on the **project's organization**. 
Global view is represented in [[Context Integration Map]].

Typically you'll define **[[Translation Layer]]** 
*for **each* integration** your [[Bounded Context|Context]] will be engaged in.

- [[Separate Ways]]
- [[Shared Kernel]]
- [[Customer-Supplier|Customer/Supplier]]
- [[Conformist]]

- [[Anti-Corruption Layer]]

- [[Open Host Service]]
- [[Published Language]]

**Relationships** offer a **trade-off**:
- *between* seamless **integration**
- *and* smooth **coordination**

![[Context Integration Strategies Demands.png]]