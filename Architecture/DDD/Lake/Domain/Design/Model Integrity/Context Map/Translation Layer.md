---
aliases:
  - Translate
  - Translator
  - Translation
---
**Translator** is the class that encapsulates **interpretation between [[Domain Model|Models]]**.

This's the only class two [[Bounded Context]] teams have to maintain together.

The **translation isn't concern of the [[Domain Model|Model]]**. This layer isn't part of [[Bounded Context]]. It's **part of the boundary** itself.

It makes sense to cover this layer with tests (make sure that it actually works).

If you need to **integrate third-party** system, you'd create an [[Anti-Corruption Layer]] [[Adapter]] that exposes **interface in our [[Ubiquitous Language|Language]]**, and **interacts** with third-party **in their [[Ubiquitous Language|Language]]**.
