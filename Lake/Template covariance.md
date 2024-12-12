> covariance is a descending (generic to concrete) variance
> 
> return types must be covariant (more specific) with interface

Covariant template `@template-covariant` allows us to pass `Collection<Dog>` into a `Collection<Animal>` type, but it doesn't allow the collection itself to have `add(T)` method.

If you have [[Template invariance|invariant template]] and still want to accept generic collection to run some code that doesn't modify the collection itself, it's possible to have **runtime covariance**.

Runtime covariance: for parameter like this `@param Collection<covariant Animal>`, we could pass an [[Template invariance|invariant]]  collection (`Collection<Dog>` or `Collection<Cat>`). And following from it calling any modification method (like `add(T)`) there would result in compile-time error (because [[Template invariance#^9212b1]] would be broken).

See [[Template contravariance]]

