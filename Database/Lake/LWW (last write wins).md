In [[Cassandra]] this is the only conflict resolution method.
In [[Riak]] this is optional method.

**Last write wins** (**LWW**) - each write is **associated with the timestamp**. On conflict, writes with more **recent timestamp wins**. 

There may even be the cases when **LWW drops writes** which are **not concurrent** (see [[LWW clock issues]]). Therefore, it should only be used where **lost writes are acceptable** (like caching).

> This method achieves **convergence** by the **cost of durability** - clients were informed that write was successful, though it is silently discarded later on. See [[LWW clock issues]].