---
aliases:
  - Lost Updates
---
**Lost Update** - when **one [[Transition]] overwrites just written updates of another [[Transition]]**. It happens in **[[Read-Modify-Write]]** cycle.

Solutions to prevent [[Lost Update|Lost Updates]]:
- [[Automatic Lost Updates prevention|Automatically (Snapshot Isolation)]];
- [[Atomic write operations]];
- [[Explicit locking]];
- [[Compare-and-Set]].

## Conflict Resolution and Replication

The only working way with **no overhead** is via of [[Atomic write operations]], especially which are **commutative** (like counter increment, addition etc).

**Neither [[Compare-and-Set]] nor [[Explicit locking]]** can help us to **prevent lost updates** in replicated systems (**[[Multi-Leader Replication|multi-leader]], [[Leaderless Replication|leaderless]]**). Therefore, it is necessary to implement **conflict resolution logic** as written previously in [[Handling write conflicts in replicated system]].
