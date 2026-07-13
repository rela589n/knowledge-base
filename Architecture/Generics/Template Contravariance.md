---
aliases:
  - Contravariant
  - Input-variance
---
**Contravariance** is an <u><b>descending</b></u> **variance** (generic to concrete)

> **Parameter types** must be contravariant (same/more generic)
> to the interface ([[Liskov substitution principle]])

This allows us to pass `Comparator<Animal>`
(some generic comparison of any animals, including dogs)
into `Comparator<Dog>` or `Comparator<Cat>`,
which is <b><u>counter-inheritance</u></b> direction.
