As far as **keys ownership** or **assignment** of partitions to nodes **may change**, clients need to know **where to send the request to**. This is a **service discovery problem**.

Options:
- clients may **send** the request **to any node** (random or selected by round-robin) and the **node will forward the request** to an authoritative node;
- the **routing tier** may be used as the **proxy to any node**. It will **forward the request** to respective node;
- **clients may know about partitioning** and send the requests to the correct node right away.

In any case, **responsible component must be notified** about any changes in the partitioning scheme: 
1. The **third-party coordination service** (like **[[ZooKeeper]]**) may be used. Every node is registered in it and **on any change** the **service notifies responsible component**. The most popular approach, used in [[HBase]], [[SolrCloud]], [[Kafka]], [[MongoDB]] (similar approach with own config);
2. Another approach is usage of **gossip protocol**. It **avoids the coordinator service** and makes every **node aware of the routing scheme**. Used in [[Cassandra]] and [[Riak]];
3. Not rebalance automaticcaly. Used in [[CouchBase]].
