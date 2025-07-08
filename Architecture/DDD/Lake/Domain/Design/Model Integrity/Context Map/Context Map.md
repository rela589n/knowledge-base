---
aliases:
  - Context Mapping
---
**[[Bounded Context|Context]] Map** is a global view the project's [[Bounded Context|Bounded Contexts]] and **relationships between them**. Useful for cross-team collaboration.

[[Code]] reuse between [[Bounded Context|Bounded Contexts]] must be avoided.

[[Context Map]] is a manager's view of the Design.
We can see what [[Bounded Context|Bounded Contexts]] and who's working on them.

**Contracts** are **touch points** between [[Bounded Context|Bounded Contexts]].
Describe them and their nature explicitly.

##### Patterns that define the nature of the *relationships between [[Bounded Context|Contexts]]*:

[[Customer-Supplier|Customer/Supplier]]

**Cooperation** - either **Partnership** or **Shared Kernel**. When teams are closely-collaborated.

**Shared Kernel** - two [[Bounded Context|bounded contexts]] physically share some parts of the code, holding shared entities.

**Partnership** - (? complete share ?)

**Conformist** - ?

[[Anti-Corruption Layer]]

[[Open-Host Service]]

**Published language** - ?

**Separate ways** - [[Bounded Context|Bounded Contexts]] are **completely independent** and have nothing shared.

