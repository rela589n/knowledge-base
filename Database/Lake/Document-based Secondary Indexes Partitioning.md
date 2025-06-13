**Local index** - each partition additionally **holds [[Secondary Index]] of its own documents** besides of the data itself.

> If DB **supports only key-value** storage, it is dangerous to implement custom secondary indexes. A **great care** is required to make them **consistent** with the **underlying data**. Issues: **race conditions**, intermittent **write failures** easily cause data get out of sync.

**Scatter-gather** - [[Secondary Index]] read approach which implies **querying all partitions for [[Secondary Index]]** to get list of used documents. It is prone to the **[[Tail Latency Amplification]]**. 
Nonetheless, it is used in [[Cassandra]] , [[VoltDB]], [[MongoDB]], [[Riak]] , [[ElasticSearch]], [[SolrCloud]].

The **benefit** is that **writes are still performant**, since [[Secondary Index]] will be maintained **per partition basis**.

The **drawback** is **worse read performance**, since [[Secondary Index]] has to be analyzed **on all partitions**.
