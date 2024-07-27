Topologies:
- **circular** (MySQL default);
- **star** - can be generalized to a tree;
- **al-to-all**;

In **circular** topology writes are propagated along with new writes of nodes, which they were propagated on (IOW, each node appends it's own replication writes).

> To prevent infinite replication loops, each write is tagged with current node identifier. If node receives writes with it's own id, these are just ignored.

If a **one node fails in *circular* or *star* topologies**, it may **interrupt the flow** of replication. Nodes may be reconfigured to communicate around a failed node, but it is mostly done manually.

The fault tolerance of more dense topologies (**all-to-all**) is better, though other **pitfalls of causality** arise.

There may be the case when some **required writes were not processed yet** on a replicated leader, while it **receives dependent writes** (like updates of rows, which were never inserted).

> ? Why won't we just append all writes to the current batch of writes the same way as in circular topology?

