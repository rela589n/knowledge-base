**Consistency** - the property of database when it **follows application [[Invariant|Invariants]]** (see [[Model Consistency]]).

It is not always enforced by the database itself, though some **constraints** may be defined (**foreign keys**, **checks**, **unique**, etc.), but usually it is **up to application to enforce** consistency rules.

If each statement of [[Transaction]] follows app [[Consistency]] rules, then on commit database will be in the Consistent state.