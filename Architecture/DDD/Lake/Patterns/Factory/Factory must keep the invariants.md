When there are a **lot of [[Invariant|Invariants]]** involved, it could make sense to check them **in the [[Factory]]**, so that main object won't be cluttered.

Yet, in case of [[Aggregate factory method]], it would make sense to keep that logic inside the object itself.

In case of Object [[Reconstitution Factory]], 
  -> [[Invariant|Invariants]] should be handled **differently**. 
  
If some [[Invariant|Invariants]] aren't met, 
we **can't** just **ignore** the existence of **this entity** in the database, 
and **can't** we **ignore** the **[[Invariant]]**, 
-> therefore some **recovering strategy** is needed for this case.
