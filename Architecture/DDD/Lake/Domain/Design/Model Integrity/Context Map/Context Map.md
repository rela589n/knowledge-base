---
aliases:
  - Context Mapping
---
**[[Bounded Context|Context]] Map** is a global view the project's [[Bounded Context|Bounded Contexts]] and **relationships between them**. Useful for cross-team collaboration.

[[Context Map]] is a manager's view of the Design.
We can see [[Bounded Context|Bounded Contexts]] and who's working on them.

Each [[Bounded Context]] must have a name and **clear Boundaries** so that team could [[Comprehension|Understand]] which part of the system each [[Bounded Context#^c073df|Aspect]] belongs to.

[[Context Map]] must **represent the situation as it is**, not as we'd like it.

[[Code]] reuse between [[Bounded Context|Bounded Contexts]] must be avoided. It's fraught with [[Integrity Problems|Model Fragmentation]] issues. Relationships must be established.

**Contracts** are **touch points** between [[Bounded Context|Bounded Contexts]].
Describe them and their nature explicitly.

[[Relationships Between Bounded Contexts]]