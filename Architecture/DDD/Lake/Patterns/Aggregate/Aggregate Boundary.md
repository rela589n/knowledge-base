Scopes the set of classes belong to this particular [[Aggregate]].

[[Aggregate Root]] is the only entity that external objects are allowed to reference.

Objects within [[Aggregate]] can hold references to other [[Aggregate Root|Aggregate Roots]]. Though, this is not allowed to reference the inner parts of the [[Aggregate]].

To define [[Aggregate Boundary]] ask the following question: what would not have existed but for this [[Aggregate Root]]?
