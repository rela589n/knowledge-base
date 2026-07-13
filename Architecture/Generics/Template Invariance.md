By default, `@template`-s are invariant.

It means that `Collection<Cat>`  and `Collection<Animal>`
are two <u>entirely different</u> things that can not be used one in stead of another (`Collection<Cat>` can not be  `Collection<Animal>`).

Rationale:
The code that accepts the abstraction (a `Collection<Animal>`) might add an instance of another concretion (`->add(new Dog)`) to it, therefore breaking the original collection (a `Collection<Cat>`). ^9212b1

See [[Template Covariance]].