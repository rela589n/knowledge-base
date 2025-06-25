**Composite** (aka **Object Tree**) is the [[GOF Design Patterns|Design Pattern]], which allows to **compose objects into tree** structures and work with them uniformly via **the same interface** as with individual objects, allowing to compose **[[Recursion|Recursive]] data structures**.

> It lets to run a recursive algorithm over a tree.

Example: admin panel that provides tree of filters that could be applied: department, city, and group filters that combine them with boolean logic.

Use it for:
- tree-like objects structure;
- when we want to treat complex compound items uniformly as a single leaves.

With [[Composite]], clients depend on an abstract type and they don't care about implementation (treat [[Polymorphism|Uniformly]]). Each concrete implementation either implements [[Composite]] operation that arches over inner structures, or just Leaf operation that returns value on their own.

