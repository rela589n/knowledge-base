Repository encapsulates infrastructural low-level job necessary for domain objects retrieval.

![[Repository.png]]

The starting point where we get the first object reference from. After having the first [[Aggregate]] reference, we could use [[Associations]] traversal to get other objects.

As a rule of thumb, no query access is needed for the objects that are more convenient to be found by [[Associations|association]] traversal.

Any object inside of the [[Aggregate]] is ***prohibited*** to be found by any other means but [[Associations|association]] traversal.

If you want to find [[Value Object]], it's questionable if it is really a value. Maybe it is an [[Entity]].

Well-designed repositories could provide [[Specification]] api.

Repositories should have the ability to be implemented in low-level queries that utilize specialized features of the inner platform.
