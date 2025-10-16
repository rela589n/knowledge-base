Distributed system **can't rely on a single node's** perception of the world, because **it may fail** and it may be **wrong in its judgements** [[Process Pauses|regarding the time]].

**Quorum** - voting among the nodes. Decisions require some **minimal number of nodes to agree** on the statement. In other words, **truth is defined by majority** (usually, half of the nodes).

For example, if [[Quorum]] nodes agree to declare some other [[Leader lease#Unexpected Expiration|node as dead]], then it has to step down and abide with [[Quorum]] decision.
