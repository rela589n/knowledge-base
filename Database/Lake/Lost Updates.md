**Lost update** - when one **concurrent transaction clobbers modifications of another** transaction. It happens in **[[read-modify-write]]** cycle.

## Solutions

See [[Solutions to lost updates]].

## Conflict Resolution and Replication

The **only working way** with no overhead is by means of **atomic operations**, especially which are **commutative** (like counter increment, addition etc).

**Neither [[Compare-and-Set]] nor [[Explicit locking]]** can help us to **prevent lost updates** in replicated systems (**[[Multi-Leader Replication|multi-leader]], [[Leaderless Replication|leaderless]]**). Therefore, it is necessary to implement **conflict resolution logic** as written previously in [[Handling write conflicts]].
