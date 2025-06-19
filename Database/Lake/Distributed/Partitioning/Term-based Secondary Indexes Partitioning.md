**Global index** - as opposed to **local index**, covers index data for all [[Partition|Partitions]]. Usually it is **term-partitioned**.

**Term-partitioned index** - such [[Secondary Index]], in which the **term determines partition** of stored value references. 

**Term partitioning** may be done **by [[Range Partitioning|terms themselves]]** (allows range scans), or **[[Hash-based Partitioning|hashes of terms]]** (better distributes the load).

The **benefit** is that **reads are performant**, since it's necessary to scan only the [[Partition|Partitions]] that hold needed [[Secondary Index]] terms.

The **drawback** is that **writes are slower and complicated**. For **index to be up to date**, it should reflect changes in the underlying data. Since it is **stored on multiple separate [[Partition|Partitions]]**, it brings **complexity of distributed transactions**.

>> **In practice**, often global [[Secondary Index|Secondary Indexes]] **updates are async**. [[DynamoDB]] does this way. It crucially dependents on reliability of the underlying **infrastructrue**.
