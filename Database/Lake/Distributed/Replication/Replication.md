---
aliases: []
---
**Replication** - *keeping* the **same data** *on* **multiple [[Replica|Replicas]]** by transmitting the [[Replication Log|Log]] over the [[Async Network|Network]].

Reasons to replicate data:
- ***reduce* [[Network Latency|latency]]** by keeping servers geographically close to the users;
- ***increase* availability** - continue operate even if some parts fail;
- ***increase* read throughput** - scale out number of nodes to serve read queries.

**Approaches**:
- **[[Single-Leader Replication|Single-Leader]]**;
- **[[Multi-Leader Replication|Multi-Leader]]**;
- **[[Leaderless Replication|Leaderless]]**.

Replication may be [[Synchronous VS Asynchronous Replication|Synchronous or Asynchronous]].

