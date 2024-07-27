Leader DB must know that it is still a leader and was not declared by other nodes as dead. For this purpose **lease** is used.

**Leader lease** - kind of **lock with timeout**, which only one node can hold at any given moment of time. Once node obtained a lease from other nodes, it has time `T` which it can process writes, also it should renew the lease within this `T`.

## Unexpected Expiration

It is important to understand that [[Process Pauses]] may cause stop of the current node, meanwhile **lease may expire** and nodes [[Quorum]] will **elect new leader**.

The fact that current node believes it has the lease, doesn't necessarily mean that [[Quorum]] nodes agree on it yet.

If **node acts as a leader not being already** and some other nodes believe it is, then system may do something incorrect and perhaps **data will get corrupted**. See [[Split Brain]].

The solution for this kind of issues is described in [[Knowledge in distributed systems#Knowledge about locks|Knowledge about locks]].