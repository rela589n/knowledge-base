**Last write wins** (**LWW**) - each **write** *has* a **ID** 
(kty-value hash / random number / uuid / **timestamp**). 
On conflict, write with **higher ID** ***wins***. 

Approach implies **data loss**.
Using [[Logical clock]] makes it more reliable.

In [[Cassandra]] - the only conflict resolution method.
In [[Riak]] - optional method.

[[Timestamps for ordering events - data loss]].

There may even be the cases when **LWW drops writes** which are **not concurrent** (see [[LWW clock issues]]). Thus, it should only be used where lost writes are acceptable (like caching).

> This method achieves **convergence** by the **cost of durability** - clients were informed that write was successful, though it is silently discarded later on. See [[LWW clock issues]].