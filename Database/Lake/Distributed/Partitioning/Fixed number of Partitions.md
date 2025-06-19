This approach is used in: [[Riak]] , [[ElasticSearch]] , [[Voldemort]], [[CouchBase]]

**By the hash of key** we decide **which [[Partition]]** to forward the request to, **not to which node**.

**Simple solution** is to **create a lot of [[Partition|Partitions]]** and place them on raletively **small amount of nodes**. When it is time to rebalance, a **new node** will be **brought in**, and some **[[Partition|Partitions]] will move** there.

**During data movement** to the new nodes **old partitions are used** for reads and writes.

For instance, if before rebalancing there were 4 nodes with 5 partitions on each, after rebalancing there would be 5 nodes with 4 partitions in each.

It's necessary to **anticipate system growth** from an outset. In future, it would be possible to have **as many nodes, as [[Partition|Partitions]]** there currently are. The number should be **big enough**, but not too big, since **each [[Partition]]** has it's own **management overhead**.
