This approach is used in: [[Riak]] , [[ElasticSearch]] , [[Voldemort]], [[CouchBase]]

**By the hash of key** we decide **which partition** to forward the request to, **not which node**. 

_Simple solution_ is to **create a lof of partitions** and place them on raletively **small amount of nodes**. When it is time to rebalance, a **new node** will be **brought in**, and some **partitions will move** to that node.

**During data movement** to the new nodes **old partitions are used** for reads and writes.

For instance, if before rebalancing there were 4 nodes with 5 partitions on each, after rebalancing there would be 5 nodes with 4 partitions in each.

It's necessary to **anticipate system growth** from an outset. In future, it would be possible to have **as much nodes, as partitions** there currently are. The number should be **big enough**, but not too big, as far as **each partition** has it's own **management overhead**.
