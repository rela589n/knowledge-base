Usually relational database is used to store the objects.
There is a mapping layer, implemented by some [[ORM]].

The key requirement for [[Domain Model]] objects is that **mapping is transparent** and that database will reveal the same model as used in the code.

Additional requirement is that our **database must not be accessed by other systems**, lest they could violate important business [[Invariant|invariants]], and besides that we'll be tied to the particular db schema (likely of last year's model) and won't be able to change it.

