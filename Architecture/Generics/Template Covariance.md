---
aliases:
  - Covariant
---
**Covariance** is an ascending variance (concrete to generic).

`@template-covariant` allows to pass `Collection<Dog>` into a `Collection<Animal>` type, but doesn't allow the collection itself to have `add(T)` method.

If you have [[Template Invariance|invariant template]] and still want to accept generic collection to run some code that doesn't modify the collection itself, it's possible to have **[[Runtime Variance]]**.

> **Return types** are covariant (same/more specific)
> to the interface ([[Liskov substitution principle]])

> **Assignment** is covariant:
> `fn(Animal $a) => $a->weight;` can accept `Cat`.
> `Animal $a = new Cat();` is allowed.
