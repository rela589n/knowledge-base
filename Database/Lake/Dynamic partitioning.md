This approach is used in: #HBase, #RethinkDB, #MongoDB 

Applicable for both [[Partitioning by Key Range|key-range partitioning]] and [[Partitioning by Hash of Key|hash-partitioning]].

If DB uses [[Partitioning by Key Range|key-range partitioning]], it may be the case when only **first partition is used**, while **others are idle**. DB may **create partitions dynamically**. When partition is **big enough, it is split**.

**Advantage** is that **number of partitions** adapts to the **amount of data**. This means, that if not set, initially DB will have a **single partition on a single node**, while **other nodes sit idle**. This can be solved with **pre-splitting**.

**Pre-splitting** - configuration of **initial set of partitions** on empty database.
