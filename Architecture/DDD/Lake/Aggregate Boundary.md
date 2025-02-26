Scopes the set of classes belong to this particular [[Aggregate]].

[[Aggregate Root]] is the only entity that outside objects are allowed to reference.

Any object of [[Aggregate]] could hold references to other [[Aggregate Root|Aggregate Roots]], yet, it is not allowed to reference the inner parts of the [[Aggregate]].

To define [[Aggregate Boundary]] we ask following question: what classes would not have existed if there were no [[Aggregate Root]]

