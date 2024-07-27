When application **reads from async follower**, the **data may differ** from if it was read **from the leader**. Though, if for example stop all writes, wait a while, then all nodes will become consistent. This is called **eventual consistency**. ^7a648b

The better name for **eventual consistency** is **convergence**.

**Convergence** - all nodes must **eventually have the same value** for each of the records. IOW, all nodes [[Converging toward a consistent state|converge toward consistent state]]. ^01eced