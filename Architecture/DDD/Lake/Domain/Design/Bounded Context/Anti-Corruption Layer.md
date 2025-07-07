---
aliases:
  - Translation Layer
---
**Anti-corruption Layer** - intermediary **translation layer** between two [[Domain Model|Models]].

For example, if we'd need to integrate third-party system with our system, we'll create some [[Facade]] layer that uses interface in our [[Ubiquitous Language|Language]], but will interact with the system in their language.

The **translation concern isn't part of the [[Domain Model|Model]]**. Thus, its layer isn't part of [[Bounded Context]]. It's part of the boundary itself.

