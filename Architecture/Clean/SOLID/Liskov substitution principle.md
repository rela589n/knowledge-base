---
aliases:
  - LSP
---
**LSP** - If we **have** an instance of **abstraction**, we could **pass *any* concretion**.

Each particular **implementation** must **follow the interface** it implements without breaking it, meaning that:
- **input parameters** must be **[[Template Contravariance|Contravariant]]** (the same type or wider) with the interface;
- **output parameters** (return values) must be **[[Template Covariance|Covariant]]** (the same or narrower) with the interface. 

Example of violation is when **interface** declares count to be returned **zero or positive**, while **implementation** could result in **negative** values, thereby violating the interface.

Also, classes that use objects of base classes should not bother themselves with particular implementations (there should be **no `instanceof`** checks) so that we **could pass any implementation.** 