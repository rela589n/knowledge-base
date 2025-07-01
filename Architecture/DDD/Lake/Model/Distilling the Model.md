[[Domain Model]] is the [[Model (generic)|Model]], - it should contain bare minimum of things that do actually closely relate to the [[Domain Concept|Domain Concepts]].

We should **drop all the excessive things** which are not important to the implementation; Everything unneeded contributes to [[Conceptual Overload]].

Each class must be understood with minimum references to the other classes. Every [[Association]] must represent **something fundamental** to the meaning of the object. 

Anything else must be [[Extracting a hidden concept|Extracted Elsewhere]]. You can [[Drawing on Established Formalisms|Draw on Established Formalisms]], and revolve it around a [[Value Object]].

[[Low Coupling & High Cohesion|Low Coupling]] is fundamental. Each [[Module]], each class must be as self-contained as possible. There must be least references to other [[Module|Modules]] and classes.


