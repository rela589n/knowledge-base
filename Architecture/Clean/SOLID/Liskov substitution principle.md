---
aliases:
  - LSP
---
**LSP** - If we **have** an instance of **abstraction**,
	we could **pass *any* concretion**.

Each **implementation** must ***follow* the interface** (not breaking it), meaning that:
- **parameters** are **[[Template Contravariance|Contravariant]]** (the same type or wider) with the interface;
- **return values** are **[[Template Covariance|Covariant]]** (the same or narrower) with the interface.

> **Example** of violation:
> 
> **Interface** declares `getCount()` to be **zero or positive**,
> but the **implementation** could return **negative** values.

Also, classes that use objects of base classes should not bother themselves with particular implementations (there should be **no `instanceof`** checks) so that we **could pass any implementation.** 
