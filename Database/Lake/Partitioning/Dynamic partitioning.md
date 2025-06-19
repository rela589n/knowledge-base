This approach is used in: [[HBase]], [[RethinkDB]], [[MongoDB]]

Applicable for both [[Range Partitioning|key-range partitioning]] and [[Hash-based Partitioning|hash-partitioning]].

If DB uses [[Range Partitioning|Key-Range Partitioning]], it may be the case that only the **first [[Partition]] is used**, while **others are idle**. DB may **create [[Partition|Partitions]] dynamically**. When [[Partition]] is **big enough, it is split**.

**Advantage** is that **number of [[Partition|Partitions]]** adapts to the **amount of data**. This also means, that if not set, initially DB will have a **single [[Partition]] on a single node**, while **other nodes sit idle**. This can be solved with **pre-splitting**.

**Pre-splitting** - configuration of **initial set of [[Partition|Partitions]]** on empty database.
