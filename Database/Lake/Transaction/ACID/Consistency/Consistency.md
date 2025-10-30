**Consistency** - the property of database when it **follows** application **[[Invariant|Invariants]]** (see [[Unified Model]]).

It is **not** always **for database** to enforce it, yet some **constraints** may be defined (**[[Foreign Key|Foreign Keys]]**, **checks**, **unique**, etc.). 

Usually it is **up to application to enforce** consistency rules.

If each statement of [[Transaction]] follows app [[Consistency]] rules, then on commit database will be in the Consistent state.
