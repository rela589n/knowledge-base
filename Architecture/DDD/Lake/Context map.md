---
aliases:
  - Context Mapping
---
[[Bounded Context|Context]] map is a representation of the project's [[Bounded Context|bounded contexts]] relationships between them and their [[Domain Model|models]] for cross-team collaboration.
##### Types of Context Mapping:

**Customer/Supplier** - one [[Bounded Context|bounded context]] (upstream) provides subset of the [[Domain Model|domain model]] to another [[Bounded Context|bounded context]] (downstream).

![[Customer-Supplier.png]]

**Shared Kernel** - two [[Bounded Context|bounded contexts]] physically share some parts of the code, holding shared entities.

**Partnership** - (? complete share ?)

**Conformist** - ?

**Anti-corruption Layer** - intermediary (translation) layer between two models.

**Open-host service** - host [[Bounded Context|bounded context]] exposes public API that could be used by other [[Bounded Context|bounded contexts]].

**Published language** - ?

**Separate ways** - [[Bounded Context|bounded contexts]] are completely independent and have nothing shared.