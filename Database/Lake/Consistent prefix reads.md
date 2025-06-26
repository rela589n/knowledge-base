There may be a **violation of causality** when the data is both **[[Partitioning|Partitioned]]** and **[[Replication|Replicated]]** and some [[Partition|Partitions]] replicate faster than others. 

Let's say there's a conversation. If the observer looks on it through the followers, then one participant replies may show up before the actual questions (the question replication lag is far greater than the reply replication lag).

**Consistent prefix reads** - type of guarantee, in which if writes were done in some order, then **reads must appear precisely in the same order**. 
This can be accomplished by enforcing all **causal writes to go into the same partition**.
