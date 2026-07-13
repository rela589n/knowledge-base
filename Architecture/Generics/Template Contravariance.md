---
aliases:
  - Contravariant
---
**Contravariance** is an <u><b>ascending</b></u> **variance** (concrete to generic)

> **Parameter types** must be contravariant (same/more generic)
> to the interface ([[Liskov substitution principle]])

This allows us to pass `Comparator<Animal>`
(some generic comparison of any animals, including dogs)
into `Comparator<Dog>` or `Comparator<Cat>`,
which is <b><u>counter-inheritance</u></b> direction.

> Function calls are covariant.
> `fn(Animal $a) => $a->weight;` can accept `Cat`.


