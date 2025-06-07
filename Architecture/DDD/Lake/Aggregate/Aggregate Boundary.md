Scopes the set of classes belong to this particular [[Aggregate]].

[[Aggregate Root]] is the only entity that external objects are allowed to reference.

Any object of [[Aggregate]] can hold reference to other [[Aggregate Root|Aggregate Roots]] (as id), yet, this is not allowed to reference the inner parts of the [[Aggregate]].

To define [[Aggregate Boundary]] ask the following question: what would not have existed but for this [[Aggregate Root]].



