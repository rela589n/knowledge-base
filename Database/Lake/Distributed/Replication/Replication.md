---
aliases: []
---
**Replication** - *keeping* the **same data** *on* **multiple [[Replica|Replicas]]** 
by transmitting the [[Replication Log|Log]] over the [[Async Network|Network]].

Reasons to replicate data:
- ***reduce* [[Network Latency|Latency]]** - keep **servers closer** to users;
- ***increase* [[Availability]]** - system operates even if some nodes are down;
- ***increase* read throughput** (**[[Scalability]]**) - serve reads from [[Replica|Replicas]], which could be scaled up;
- **disconnected operation** - app continues to work even though there are network issues.

A bare minimum for app using replication is to **deal with**:
- **network issues**
- **nodes outage**

**Types**:
- **[[Single-Leader Replication|Single-Leader]]**;
- **[[Multi-Leader Replication|Multi-Leader]]**;
- **[[Leaderless Replication|Leaderless]]**.

**Synchronization types** ([[Synchronous vs Asynchronous Replication|Synchronous vs Asynchronous]]):
- **sync** - not that fast as async, badly handles nodes outages;
- **async** - requires anticipating app behavior when [[Problems with Replication Lag|Replication Lag]] increases.

Replication **consistency models**:
- **[[Reading your writes]]** - users ***see* their submitted data**.
- **[[Monotonic reads]]** - once displayed to the user, the  **information** should ***not** be* ***any*** ***staler** than* already *shown* to him;
- **[[Consistent prefix reads]]** - [[Causality|Causal]] dependencies must be kept (question message comes first, then answer).

In **[[Multi-Leader Replication|Multi-Leader]] and [[Leaderless Replication|Leaderless]]** replication types the **conflicts may arise**. To solve them one can use:
- **automatic** conflict resolution (like [[LWW (last write wins)]], usage of **[[Conflict-free Replicated Data Types|CRDTs]]**);
- **manual** resolution with **[[Version Numbers|Versions]]** and **[[Version Vectors]]**.
