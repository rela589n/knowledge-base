[[Entity deletion happens last]]

[[Doctrine Custom Collections]]

[[Change Sets Calculated on every flush()|Flush Change Sets]]

[[N+1 Problem]]

[[Identity map lookup limitations]]

[[Lazy Criteria API limitations]]

[[Lack of async support]]

[[Partial Hydration]]

[[Doctrine ORM directory mappings without separate folder]]

[[Entity Inheritance - Inoptimal Join condition]]

Entity Inheritance - many to one to an abstract class is the worst case for performance - it is loaded right away, and results in [[N+1 Problem]] during hydration. This is not possible in [[Doctrine ORM]] because proxy class must know what particular instance to target, while id is not enough. It could've been avoided had this field been not hydrated right away.

[[Doctrine Foreign Key to Unique Column rather than Primary Key]]

[[Doctrine ORM Entity Change Discriminator Column|Entity Change Discriminator Column]]

[[Composite Primary Key Limitations]]

[[Doctrine ORM multiple Entities for the same table]]

[[Flush one entity]]

[[Symfony Doctrine Type Dependency Injection]]

[[Mapping Types Strangeness]]