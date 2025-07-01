---
aliases:
  - Object Tree
  - Compose
---
**Composite** is a [[GOF Design Patterns|Design Pattern]], that allows you to **compose objects into tree** of **[[Recursion|Recursive]] data structures** and work with them [[Polymorphism|Uniformly]] via **the same interface** as with individual objects.

Use it when [[Composite]] data structures can be asked **the same questions** as Leaf data structures. The interface must represent [[Conceptual Boundary|Conceptual Contour]].

With [[Composite]], clients **depend on an abstract type** ([[DIP]]) and they don't care about implementation (treat [[Polymorphism|Uniformly]]). Each concrete **operation** either **arches over inner structures** (possibly [[Recursion|Recursively]]) in case of [[Composite]], or just **returns value on their own** in case of Leaf.

> **Example:** admin panel that provides [[Composite]] [[Specification]] of **filters** that can be applied: department, city, and you can **[[Composite|Compose]] them** with boolean logic ([[Predicate#^6640e7]]).

Use it for:
- tree-like objects structure;
- when we want to treat complex compound items uniformly as a single leaves.





