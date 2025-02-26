**Lost update** - when one **concurrent transaction overwrites the updates of another** transaction. It happens in **[[read-modify-write]]** cycle.

## Solutions

Solutions to prevent lost updates:
- [[Automatic lost updates prevention|Automatically (snapshot isolation)]];
- [[Atomic write operations]];
- [[Explicit locking]];
- [[Compare-and-Set]].

## Conflict Resolution and Replication

The **only working way** with no overhead is by means of **atomic operations**, especially which are **commutative** (like counter increment, addition etc).

**Neither [[Compare-and-Set]] nor [[Explicit locking]]** can help us to **prevent lost updates** in replicated systems (**[[Multi-Leader Replication|multi-leader]], [[Leaderless Replication|leaderless]]**). Therefore, it is necessary to implement **conflict resolution logic** as written previously in [[Handling write conflicts in replicated system]].
