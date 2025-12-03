---
aliases:
  - Covariant
---
**Covariance** is a descending variance (generic to concrete).

> **Return types** must be covariant (more specific)
> to the interface ([[Liskov substitution principle]])

Covariant template `@template-covariant` allows us to pass `Collection<Dog>` into a `Collection<Animal>` type, but it doesn't allow the collection itself to have `add(T)` method.

If you have [[Template Invariance|invariant template]] and still want to accept generic collection to run some code that doesn't modify the collection itself, it's possible to have **[[Runtime Variance]]**.
