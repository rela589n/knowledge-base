---
aliases:
  - Map Relationship
  - Bounded Context Relationships
  - Integration Strategies
  - Integration Relationships
---
**Context Strategies** are Patterns that define the nature of the **relationships between [[Bounded Context|Bounded Contexts]]**. They mostly depend on the **project organization**. Global view is shown in [[Context Integration Map]].

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

See [[Bounded Context Boundaries]], [[External Systems Integration]]

When to [[Bounded Context|Bounded Contexts]] have related [[Domain Model|Models]], it's possible that each develops its own fine-tuned [[Ubiquitous Language|Language]] (like [[Model Unification#^4c61c2|Elephant]]). 
It's fraught with:
- loss of [[Ubiquitous Language|Shared Language]] reduces communication;
- overhead of [[Translation Layer|Translation]] during [[Context Integration Map|Integration]];

How valuable is this jargon, peculiar to the [[Bounded Context]]? Sometimes it's just more trouble than it's worth.
