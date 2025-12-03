---
aliases:
  - Object Tree
  - Compose
  - Tree
---
**Composite** allows you to:
- ***compose*** objects *into* a **tree** of **[[Recursion|Recursive]] data structures**;
- and *work **[[Polymorphism|Uniformly]]*** *with* **compound** objects
  ***as** with* **individual** (same interface, [[Dependency inversion principle|DIP]]).

Clients ***depend on*** an **abstract type** ([[Dependency inversion principle|Dependency Inversion]])
and don't care about implementation ([[Polymorphism]]).

Each **operation** either:
- [[Composite]]: ***arches over*  inner structures** (possibly [[Recursion|Recursively]])
- Leaf:  *or* just ***returns* value** on their own.

> **Example:** admin panel that provides **[[Composite]] Filters**
> ([[Specification]] can be: department, city).
> You can **[[Composite|Compose]] them** with boolean logic ([[Predicate#^6640e7]]).

**Supported by**: [[Prototype]], [[Visitor]].

The interface represents [[Conceptual Boundary|Conceptual Contour]].
Use when **[[Composite]] structures** can be **asked** the **same questions** as **Leaf** data structures. 

