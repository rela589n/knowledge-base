> contravariance is an ascending (concrete to generic) variance
> 
> parameter types must be contrvariant (more generic) with interface

It would allow us to pass `Comparator<Animal>` into a parameter that expects `Comparator<Dog>`, which is counter-inheritance direction.

It is useful, since when you have a generic `Comparator<Animal>` that could compare any two animals regardless of their types, why wouldn't we allow it to be used in place of any concrete expected parameter like `Comparator<Dog>`.
