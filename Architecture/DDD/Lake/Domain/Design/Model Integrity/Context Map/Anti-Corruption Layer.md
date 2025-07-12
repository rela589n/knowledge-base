---
aliases: []
---
**Anti-corruption Layer** - [[Model Context Strategies|Relationship]] that anticipates severe intermediary **[[Translation Layer|Translation]]** mechanism between two [[Domain Model|Models]] to protect our [[Domain Model|Model]] from external influence.

When **integrating legacy system**, if it's a large scope of integration, **their [[Domain Model|Model]] may leak** into our [[Domain Model|Model]]. When interacting with them, we **need to adapt** to their semantics.

It's clear that if you take **data** from one system and **misinterpret it** in another, it **results in errors** and **corruption**. Much more if **[[Domain Model|Domain Models]] are different**, they must be **[[Translation Layer|Translated]]** and interpreted appropriately.

This layer usually is represented as set of [[Service|Services]] (not even single component), each doing [[Translation Layer|Translation]]. 

There are three main [[Service|Services]]:
- [[Adapter]]
- [[Facade]]
- [[Translation Layer|Translator]]

Sometimes third-party exposes fuzzy **interfaces** that're **hard to deal with**. These should be encapsulated in **[[Facade|Facades]]** that present **friendly interface**. These belong to their [[Bounded Context]], and therefore must **written strictly in other system's [[Domain Model|Model]]**.

To expose **interface in terms of our [[Domain Model|Model]]**, yet interact with their [[Domain Model|Model]], we should **use [[Adapter|Adapters]]**. These expose known interface, but operate with system in their interface, and convert results back to our interface.

Then, dedicated [[Translation Layer|Translator]] holds the responsibility of cross-[[Domain Model|Model]] conversion.

![[Anti-Corruption Layer.png]]

Technically, [[Anti-Corruption Layer]] can be placed:
- within the subsystem;
- as a separate subsystem.

[[Anti-Corruption Layer]] can be extended with Audit trail.
Also, [[Anti-Corruption Layer]] can be between your own [[Bounded Context|Bounded Contexts]] in case they've deviated ([[Separate Ways]]).
