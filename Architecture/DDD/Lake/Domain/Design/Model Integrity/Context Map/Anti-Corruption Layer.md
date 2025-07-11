---
aliases: []
---
**Anti-corruption Layer** - [[Relationships Between Bounded Contexts|Relationship]] that anticipates severe intermediary mechanism for **[[Translation Layer|Translation]]** between two [[Domain Model|Models]].

Sometimes it's necessary to **integrate legacy system**. If it's a **large scope of integration**, and we **need to adapt** to their semantics, **their [[Domain Model|Model]] may leak** into our [[Domain Model|Model]].

It's clear that if you take **data** from one system and **misinterpret it** in another, it **results in errors** and **corruption**. Much more if **[[Domain Model]]**'s different, it must be **[[Translation Layer|Translated]] and interpreted appropriately**.

This layer usually is represented as set of [[Service|Services]] (not even single component), each doing [[Translation Layer|Translation]]. These are [[Facade|Facades]], [[Adapter|Adapters]]

Sometimes third-party exposes fuzzy interfaces hard to deal with. These can be encapsulated in [[Facade|Facades]].

