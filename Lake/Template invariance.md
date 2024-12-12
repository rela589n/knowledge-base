By default, `@template`-s are invariant, meaning that `Collection<Animal>` and `Collection<Cat>` are two entirely different things that could not be used interchangeably.

From this follows that `Collection<Animal> $animals` could not accept `Collection<Dog>`. 

The explanation for this is that method could add the instance of another subtype of the generic, therefore breaking the original collection. ^9212b1

Having `Collection<Animal> $animals`, we could: `$animals->add(new Cat)`. And if pass there a collection of Dogs, after this method call, it would not have been a `Collection<Dog>` any longer (therefore, it's not possible).

See [[Template covariance]].