**Consistency** - the property of database when it **follows application [[Invariant|invariants]]**. 

It is not always enforced by the database itself, though some **constraints** may be defined (**foreign keys**, **checks**, **unique**, etc.), but usually it is **up to application to enforce** consistency rules.

If each statement of transaction follows app consistency rules, then after commit database will be in the consistent state.