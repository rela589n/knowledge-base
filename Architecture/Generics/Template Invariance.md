By default, `@template`-s are invariant, meaning that `Collection<Animal>` and `Collection<Cat>` are two entirely different things that could not be used interchangeably.

From this follows that `Collection<Animal> $animals` could not accept `Collection<Dog>`. 

The explanation for this is that this method could possibly add the instance of another subtype (like Cat) of that generic, therefore breaking the original collection (of Dogs). ^9212b1

IOW, Having `Collection<Animal> $animals`, we could: `$animals->add(new Cat)`. And if pass there a collection of Dogs, after this method call, it would not be a `Collection<Dog>` any longer. Therefore, it's prohibited.

See [[Template Covariance]].