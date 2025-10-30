**Failover** - process when system has to **promote one** of the followers **to be the leader** when such failed. Clients should send their writes to new leader, other followers should start consuming data changes from new leader.

Automatic:
1. Detect that **leader has failed** - if node doesn't respond for some **timeout** (e.g. 30 seconds), it is considered dead;
2. **Choose new leader** - who to chose could be decided with [[Quorum|Election Process]] (who most [[Replica|Replicas]] agree on), or a leader could be chosen by previously elected *controller node*;
3. **Reconfigure system** to the new leader. Clients have to send requests to the new leader. If old leader comes back, it has to become follower of a new leader.

Pitfalls:
- If a **new leader did not receive all updates** from the old one and old comes back - it's data updates may **conflict with existing data**. In this case, usually such **data is discarded**, which violates durability;
- **Discarding** writes is **especially dangerous** if there are some **other correlated with DB system**. Say, [[Redis]] may store incremental IDs, which were discarded because of failover and new same ID are written later on - this may lead to **information disclosure**.
- In some fault scenarios, **[[Split Brain]] is possible**.
- With too **short [[Network Timeouts|timeout]]** to detect dead leader, there could be **unnecessary failovers**. Making it **too long** means **longer recovery** in case where leader fails.

There are **no easy solutions** for this kind of problems. That's why some operations teams prefer to **do manual failovers**, even if system supports automatic.
