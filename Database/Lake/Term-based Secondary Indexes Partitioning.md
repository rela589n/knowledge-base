**Global index** - as opposed to **local index**, covers index data for all partitions. Usually it is **term-partitioned**.

**Term-partitioned index** - such secondary index, in which the **term determines partition** of stored value references. 

**Term partitioning** may be done **by [[Partitioning by Key Range|terms themselves]]** (allows range scans), or **[[Partitioning by Hash of Key|hashes of terms]]** (better distributes the load).

The **benefit** is that **reads are performant**, since it's necessary to scan only partitions which hold needed secondary index terms.

The **drawback** is that **writes are slower and complicated**. For **index to be up to date**, it should reflect changes to underlying data. Since it is **stored on multiple separate partitions**, it brings **complexity of distributed transactions**.

>> **In practice**, often global secondary indexes **updates are async**. #Dynamo does this way. It is very **prone to the infrastructrue** reliability.
