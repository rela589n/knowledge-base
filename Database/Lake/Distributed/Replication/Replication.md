---
aliases:
  - Replica
---
**Replication** - keeping the same **data on multiple machines**, that are connected via a [[Async networks|network]].

**Replica** - each node that stores copy of data.

Reasons to replicate data:
- **reduce [[Network Latency|latency]]** for users by keeping servers geographically close to them;
- **increase availability** - continue operate even if some parts fail;
- **increase read throughput** - scale out number of nodes to serve read queries.

Approaches to *replicate changes*:
- **[[Single-Leader Replication|single-leader]]**;
- **[[Multi-Leader Replication|multi-leader]]**;
- **[[Leaderless Replication|leaderless]]**.

There are multiple [[Implementation of Replication Logs|ways to replicate changes]].
Replication may be [[Sync VS Async Replication|synchronous or asynchronous]].
Async replication means solving [[Problems with Replication lag|problems with replication lag]].
