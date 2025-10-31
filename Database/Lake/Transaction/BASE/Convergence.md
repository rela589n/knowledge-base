---
aliases:
  - Eventual Consistency
  - Convergent
---
**Convergence** - all nodes must **eventually have the same value** for each record. They [[Converging toward a consistent state|Converge toward consistent state]].

When application **reads from async follower**, the **data may differ** from if it was read **from the leader**. Yet, if for example we stop all writes and wait a while, then all nodes will eventually become consistent. This is called **eventual consistency**. ^7a648b

The better name for **eventual consistency** is **convergence**.
