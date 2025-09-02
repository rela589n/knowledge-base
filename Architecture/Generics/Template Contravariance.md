---
aliases:
  - Contravariant
---
> Contravariance is an ascending (concrete to generic) variance
> 
> parameter types must be contrvariant (more generic) with the interface ([[Liskov substitution principle]])

This allows us to treat `Comparator<Animal>` (comparison of any animals, including dogs) as `Comparator<Dog>`, which is counter-inheritance direction.

It is useful, since when you have a generic `Comparator<Animal>` that could compare any two animals regardless of their types, so we can use it in any place, including `Comparator<Dog>`, `Comparator<Cat>`, or any other.
