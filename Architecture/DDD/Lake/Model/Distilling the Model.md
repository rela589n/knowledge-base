[[Domain Model]] is the [[Model (generic)|Model]], - it should not contain excessive things that do not actually closely relate to the [[Domain Concept|Domain Concepts]].

We should **drop the excessive things** which are not important to the implementation; Every unneeded thing contributes to [[Conceptual Overload]].

Each class must be understood with minimum references to the other classes. Every [[Association]] must represent something fundamental to the meaning of the object.

[[Low Coupling & High Cohesion|Low Coupling]] is fundamental. Each [[Module]], each class must be as self-contained as possible. There must be least references to other [[Module|Modules]] and classes.
