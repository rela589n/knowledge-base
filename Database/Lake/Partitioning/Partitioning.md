**Sharding** - breaking the data into **partitions**.
**Partition** - the same as **shard**, **region**, **tablet**, **vnode**, **vbucket**. Each partition is a small database on it's own, which holds some subset of records.

Main reason for partitioning is **[[Scalability|scalability]]**.

See [[Partitioning and Replication]].
See [[Partitioning Split Approaches]].
See [[Relieving Skewed Workloads]].
See [[Partitioning and Secondary Indexes]].
See [[Partitioning Strategies for Rebalancing]].
See [[Partitions Request Routing]].
See [[Parallel Query Execution]].