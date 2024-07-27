**[[Quorum]] reading and writing** - If there are `N` replicas, every **write must be confirmed by `W` nodes**, and **at least `R` nodes must be queried** for each read.

As long as `R + W > N` , the reads are guaranteed to be up-to-date, because in system there may be **no more than `N - W` stale replicas**.

> Usual choice is to set `R = W = (N + 1) / 2`, where `N & 1`. Though, in systems where writes are rare, it would make sense for `W` to approach to `N`, hence reads will be faster.

Fault tolerance:
- if `W < N`, we can tolerate `N - W`  unavailable nodes;
- if `R < N`, we can tolerate `N - R` unavailable nodes.

There are some [[Limitations of Quorum consistency]].