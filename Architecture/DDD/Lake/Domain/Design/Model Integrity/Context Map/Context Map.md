---
aliases:
  - Context Mapping
---
**[[Bounded Context|Context]] Map** is a global view the project's [[Bounded Context|Bounded Contexts]] and **relationships between them**. Useful for cross-team collaboration.

[[Code]] reuse between [[Bounded Context|Bounded Contexts]] must be avoided.

**Contracts** are **touch points** between [[Bounded Context|Bounded Contexts]].

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

