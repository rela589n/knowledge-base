Repository encapsulates infrastructural low-level job necessary for domain objects ([[Aggregate Root]]) retrieval.

![[Repository.png]]

The starting point where we get the first object reference from. After having the first [[Aggregate Root]] reference, we could use [[Association Traversal]] to get other objects.

As a rule of thumb, no query access is needed for the objects that are more conveniently found by [[Association Traversal]].

Any object inside of the [[Aggregate]] is ***prohibited*** to be found by any other means but by [[Association Traversal]].

The client of the repository should think as if the objects were all in memory, and repository was just filtering them.

If you want to find [[Value Object]], it's questionable if it is really a value. It's likely to be an [[Entity]].

Well-designed repositories could provide [[Specification]] api.

Repositories should have the ability to be implemented in low-level queries that utilize specialized features of the inner platform.
