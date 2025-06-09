A single, specific [[Entity]] in the [[Aggregate]] that is the **owner of all other entities**. Only [[Aggregate Root]] has **its own identity**.

Other entities could have local identity, distinguishable only within current aggregate, but [[Aggregate root has global identity]].

It's usually [[Aggregate Root]] that [[Locking Schemes]] are applied to, in particular [[Optimistic Locking]].
