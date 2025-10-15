---
aliases: []
---
**Replication** - keeping the same **data on multiple machines** ([[Replica|Replicas]]), that are connected via a [[Async Networks|network]].

Reasons to replicate data:
- ***reduce* [[Network Latency|latency]]** by keeping servers geographically close to the users;
- ***increase* availability** - continue operate even if some parts fail;
- ***increase* read throughput** - scale out number of nodes to serve read queries.

**Approaches** to replicate changes:
- **[[Single-Leader Replication|Single-Leader]]**;
- **[[Multi-Leader Replication|Multi-Leader]]**;
- **[[Leaderless Replication|Leaderless]]**.

There are multiple [[Replication Strategies|Ways To Replicate Changes]].
Replication may be [[Synchronous VS Asynchronous Replication|Synchronous or Asynchronous]].

