---
aliases:
  - Map Relationship
  - Bounded Context Relationships
  - Integration Strategies
  - Integration Relationships
  - Map Strategies
---
**Context Integration Strategies** are Patterns that define the nature of the **relationships between [[Bounded Context|Bounded Contexts]]**. They mostly depend on the **project's organization**. Global view is shown in [[Context Integration Map]].

Typically you'll define [[Translation Layer]] for each integration your [[Bounded Context|Context]] will be engaged in.

- [[Shared Kernel]]
- [[Customer-Supplier|Customer/Supplier]]
- [[Conformist]]
- [[Anti-Corruption Layer]]
- [[Separate Ways]]

- [[Open Host Service]]
- [[Published Language]]

**Cooperation** - either **Partnership** or **Shared Kernel**. When teams are closely-collaborated.

**Partnership** - (? complete share ?)

[[External Systems Integration]]

[[Bounded Context Boundary|Bounded Context Boundaries]]

When integrating our [[Bounded Context|Bounded Contexts]], it's important to understand that **we have much more freedom** than in case of [[External Systems Integration]]. When integration is needed, we can jointly create **simple [[Translation Layer]]**, and adjust both [[Bounded Context|Bounded Contexts]].
