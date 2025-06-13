If `W + R <= N`, then **[[Quorum]] condition** is not satisfied. Though, it allows to reduce latency and increase availability.

There may be edge cases even when **[[Quorum]] condition is satisfied**, but **stale reads are still possible**:
- a **sloppy [[Quorum]]** is used - the `W` writes may end up on different nodes, than used by `R` reads;
- on **concurrent writes** - not clear which one happened fist;
- on **race condition between read and write** - write may be reflected only on some replicas;
- if **write has failed** on some of the nodes `W` is not fulfilled, the writes on succeeded nodes is **not rolled back**. Reads may or may not return new data;
- if the **node carrying write** fails, and is restored from stale node, the [[Quorum]] condition may be **no longer satisfied**.

**Staleness monitoring** for leaderless systems is quite hard. There are **almost no tools** for it.
