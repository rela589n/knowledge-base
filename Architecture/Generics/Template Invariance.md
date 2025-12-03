By default, `@template`-s are invariant,
meaning that `Collection<Animal>` and `Collection<Cat>` 
are two <u>entirely different</u> things that can not be used interchangeably.

Thus, `Collection<Dog>` could not be  `Collection<Animal>`. 

Rationale: method might add an instance of another subtype (like Cat) to that collection,
therefore breaking the original collection (of Dogs). ^9212b1

IOW, Having `Collection<Animal> $animals`, we could: `$animals->add(new Cat)`. And if pass there a collection of Dogs, after this method call, it would not be a `Collection<Dog>` any longer. Therefore, it's prohibited.

See [[Template Covariance]].