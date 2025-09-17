---
aliases:
  - Object Tree
  - Compose
  - Tree
---
**Composite** allows you to:
- **compose** objects into a **tree** of **[[Recursion|Recursive]] data structures**;
- and **[[Polymorphism|Uniformly]]** work with **compound** objects **as** with **individual**  via the **same interface** ([[Dependency inversion principle|DIP]]).

Clients **depend on** an **abstract type** ([[Dependency inversion principle|Dependency Inversion]]) and they don't care about implementation ([[Polymorphism]]).

Each **operation** either **arches over inner structures** (possibly [[Recursion|Recursively]]) in case of [[Composite]], or just **returns value on their own** in case of Leaf.

> **Example:** admin panel that provides [[Composite]] **Filters** [[Specification]] that can be applied: department, city, and you can **[[Composite|Compose]] them** with boolean logic ([[Predicate#^6640e7]]).

Useful with [[Prototype]], [[Visitor]].

Use when **[[Composite]] structures** can be **asked** the **same questions** as **Leaf** data structures. The interface must represent [[Conceptual Boundary|Conceptual Contour]].

