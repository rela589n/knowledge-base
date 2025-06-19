[[Partitions Rebalancing|Rebalancing]] is an **expensive operation**, because it requires a lot of data migration, which **increases the load on the network and on the nodes** and requires **requests rerouting**. 

Fully **automated [[Partitions Rebalancing|Rebalancing]] is unpredictable**. 

If it will happen during system peak time, it may **lay down the whole system**. When one node is overloaded and slows down to respond, other nodes may think it is dead and move load away from it, in turn slowing down other nodes.  As the outcome we may have **cascade failure**.

[[CouchBase]], [[Riak]], [[Voldemort]] can generate suggested partition-node assignment automatically, but **require administrator to apply it**. That's the **best trade-off** between automatic and manual rebalancing.
