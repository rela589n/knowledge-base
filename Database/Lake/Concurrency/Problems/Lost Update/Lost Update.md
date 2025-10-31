---
aliases:
  - Lost Updates
---
**Lost Update** - **[[Transaction]] *overwrites*** *just written* **changes *of* another**. It happens in **[[Read-Modify-Write]]** cycle.

Preventing:
- [[Automatic Lost Update Prevention|Automatically (Snapshot Isolation)]];
- [[Atomic write operations]];
- [[Explicit locking]];
- [[Compare-and-Set]].

## Conflict Resolution and Replication

The only working way with **no overhead** is via of [[Atomic write operations]], especially **commutative** (like counter increment, addition etc).

**Neither [[Compare-and-Set]] nor [[Explicit locking]]** can help to **prevent [[Lost Update|Lost Updates]]** in replicated systems (**[[Multi-Leader Replication|multi-leader]], [[Leaderless Replication|leaderless]]**). It is necessary to implement **conflict resolution logic** as written in [[Handling write conflicts in Replicated system]].
