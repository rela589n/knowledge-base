Each datacenter may have one leader, and multiple followers. Leaders will synchronize between each other.

- **performance** - since writes go to the local datacenter leader, it is faster than if directed to the single datacenter;
- **tolerance of datacenter outages** - when some datacenter with the leader fails, system will continue it's operation, once it comes back online, replication catches up;
- **tolerance of network problems** - temporary network interruption does not prevent writes from being processed.

Multi-leader tools:
- Tungsten Replicator (MySQL);
- BDR (PostgreSQL);
- GoldenGate (Oracle).

The **main downside** is that multiple leader nodes **may update the same data** - the **write conflicts** must be resolved.

> Auto-incrementing keys, triggers, integrity constraints are problematic with multi-leader replication, therefore this kind of replication **should be avoided if possible**.
