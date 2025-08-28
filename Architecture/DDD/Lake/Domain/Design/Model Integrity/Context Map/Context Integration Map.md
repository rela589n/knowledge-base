---
aliases:
  - Context Mapping
  - Integration
  - Model Map
  - Domain Integration
---
**[[Bounded Context|Context]] Map** is a global view the project's [[Bounded Context|Bounded Contexts]] and **[[Context Integration Strategies|Integration Relationships]] between them**. Useful for cross-team collaboration.

[[Context Integration Map]] is a **manager's view** of the Design.
We can see [[Bounded Context|Bounded Contexts]] and **who's working** on them.

Each [[Bounded Context]] must have a name and **clear [[Bounded Context Boundary|Boundaries]]** so that team could [[Comprehension|Understand]] which part of the system each [[Bounded Context Aspects|Aspect]] belongs to.

[[Context Integration Map]] must **represent the situation as it is**, not as we'd like it.

Direct [[Code]] reuse between [[Bounded Context|Bounded Contexts]] is prohibited. 
It's fraught with [[Model Contradictions|Model Fragmentation]] issues. **Relationships** must be established with [[Context Integration Strategies]].

**Contracts** are **touch points** between [[Bounded Context|Bounded Contexts]].
Describe them and their nature explicitly.

