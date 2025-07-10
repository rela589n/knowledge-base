---
aliases: []
---
**Anti-corruption Layer** - [[Relationships Between Bounded Contexts|Relationship]] that anticipates intermediary aggressive **[[Translation Layer]]** between two [[Domain Model|Models]].

Sometimes it's necessary to **integrate legacy system**. If it's a **large scope of integration**, and we **need to adapt** to their semantics, **their [[Domain Model|Model]] may leak** into our [[Domain Model|Model]].

It's clear that if you take **data** from one system and **misinterpret it** in another, it **results in errors** and **corruption**. Much more is **[[Domain Model]]** different, and it must be **[[Translation Layer|Translated]] appropriately**.
