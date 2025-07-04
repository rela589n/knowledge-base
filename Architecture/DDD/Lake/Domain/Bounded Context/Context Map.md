---
aliases:
  - Context Mapping
---
**[[Bounded Context|Context]] Map** is a representation of the project's [[Bounded Context|Bounded Contexts]] signifying **relationships** between them and their [[Domain Model|Models]] for cross-team collaboration.

**Contracts** are **touch points** between [[Bounded Context|Bounded Contexts]].

##### Types of Context Mapping:

**Customer/Supplier** - one (upstream) [[Bounded Context]] **provides subset of the [[Domain Model|Domain Model]] to another** (downstream) [[Bounded Context]].

![[Customer-Supplier.png]]

**Cooperation** - either **Partnership** or **Shared Kernel**. When teams are closely-collaborated.

**Shared Kernel** - two [[Bounded Context|bounded contexts]] physically share some parts of the code, holding shared entities.

**Partnership** - (? complete share ?)

**Conformist** - ?

[[Anti-Corruption Layer]]

[[Open-Host Service]]

**Published language** - ?

**Separate ways** - [[Bounded Context|Bounded Contexts]] are **completely independent** and have nothing shared.

