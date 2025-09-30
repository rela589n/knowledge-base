---
aliases:
  - Context Map Relationship
  - Bounded Context Relationships
  - Integration Strategies
  - Integration Relationships
  - Context Map Strategies
---
**Context Integration Strategies** are Patterns that define the nature of the **relationships between [[Bounded Context|Bounded Contexts]]**.
They depend mostly on the **project's organization**. 
Global view is represented in [[Context Integration Map]].

Typically you'll define [[Translation Layer]] for each integration your [[Bounded Context|Context]] will be engaged in.

- [[Separate Ways]]
- [[Shared Kernel]]
- [[Customer-Supplier|Customer/Supplier]]
- [[Conformist]]

- [[Anti-Corruption Layer]]

- [[Open Host Service]]
- [[Published Language]]

**Cooperation** - either **Partnership** or **Shared Kernel**. When teams are closely-collaborated.

**Partnership** - (? complete share ?)

[[External Systems Integration]]

[[Bounded Context Boundary|Bounded Context Boundaries]]

When *integrating* **own [[Bounded Context|Bounded Contexts]]**, 
we *have* **more freedom** *than* in case of **[[External Systems Integration|External]]**:
- we can jointly develop **simple [[Translation Layer]]**
  *and* **adjust** both [[Bounded Context|Contexts]]

In relationships there's a **trade-off**:
- *between* seamless **integration**
- *and* smooth **coordination**

![[Context Integration Strategies Demands.png]]