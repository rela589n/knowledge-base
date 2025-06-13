#Dynamo, [[Riak]], [[Cassandra]], #Voldemort

If the client faces network interruption, a lot of alive nodes may look like dead to him. Though, for other clients they are still alive.

**Sloppy quorum** (not actually the [[Quorum]]) - when `R` or `W` can't be reached on `N` designated nodes, the **requests are sent to other nodes**, which are **not in the list** of _designated_.

**Hinted handoff** - once issue with `N` main nodes is fixed, **sloppy quorum writes** are sent to their **home nodes** (`N`).

> Sloppy quorums does not guarantee up-to-date read (even when `W + R >N`), because writes may've been **sent to the neighbour nodes** (outside of `N`). Hence, sloppy quorum is not really a quorum - it is just durability assurance that values are written somewhere.

## Multi-datacenter operation

[[Cassandra]] and #Voldemort provide next model for **multi-datacenter replication**:

The `N` is selected among nodes in all datacenters. In configuration we select **how many nodes to wait for each datacenter**.

Usual case is when reads and **writes wait for local datacenter replicas**, because it's not affected by cross-datacenter network issues. The high-latency writes to other datacenters are usually configured to happen in async manner.