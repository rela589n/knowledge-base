In case if there are a lot of [[Invariant|invariants]] involved, it could make sense to keep their check inside the factory, so that main domain object won't be cluttered.

Yet, in case of [[Aggregate factory method]], it would make sense to keep that logic inside the object itself.

In case of [[Reconstitution Factory]], [[Invariant|invariants]] should be handled differently. If some invariant isn't met, we can't just ignore the existence of the entity in the database, but have some recovering strategy instead.
