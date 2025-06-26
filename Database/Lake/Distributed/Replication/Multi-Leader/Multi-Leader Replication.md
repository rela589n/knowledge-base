---
aliases:
  - Master-Master Replication
---
**Multi-leader** [[Replication]] - **multiple nodes accept writes**, each of them forwards data to other nodes. Each leader may act as a follower to another leader.

This [[Use-cases for Multi-Leader-Replication|multi-leader replication use cases]] benefits rarely outweigh the complexity, therefore it is **not much used**.

With multi-leader replication its very likely that [[Handling write conflicts in replicated system|conflicts must be handled]].

The log stream must somehow go from one leader to all others. See [[Multi-leader Replication Topologies]].
