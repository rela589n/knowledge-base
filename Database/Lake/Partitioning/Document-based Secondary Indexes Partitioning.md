**Local index** - each [[Partition]] additionally **holds [[Secondary Index]] of its own documents** besides of the data itself, and uses [[Scatter-gather]] to read.

> If DB **supports only key-value** storage, it is dangerous to implement custom secondary indexes. A **great care** is required to make them **consistent** with the **underlying data**. Issues: **race conditions**, intermittent **write failures** easily cause data get out of sync.

Used in [[Cassandra]] , [[VoltDB]], [[MongoDB]], [[Riak]] , [[ElasticSearch]], [[SolrCloud]].

The **benefit** is that **writes are still performant**, since [[Secondary Index]] will be maintained **on per [[Partition]] basis**.

The **drawback** is **worse read performance**, since [[Secondary Index]] has to be analyzed **on all [[Partition|Partitions]]**.
