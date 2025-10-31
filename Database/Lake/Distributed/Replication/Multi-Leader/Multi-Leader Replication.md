---
aliases:
  - Master-Master Replication
---
**Multi-leader [[Replication]]** - **multiple masters accept writes**, each's forwarding data to other nodes. Each leader may act as a follower to another leader.

These [[Use-cases for Multi-Leader-Replication|Multi-Leader Replication use case]] benefits rarely outweigh the **complexity**, therefore it is **not much used** -[[Handling write conflicts in Replicated system|Conflicts must be handled]].

The log stream must somehow go from one leader to all others. See [[Multi-leader Replication Topologies]].
