---
aliases:
  - Relieving Skewed Workloads
---
**Skewed [[Partitioning]]**  - when some [[Partition|Partitions]] **have more data or queries** than others.

Even with [[Hash-based Partitioning|Partitioning by Hash of Key]], there may be **extreme [[Hot spot]] cases** when reads and writes are **for the same key** (e.g. some celebrity).

To **distribute the workload** there's **no easy solution**. The only way to handle it is to write custom **application code**, which will **reduce the [[Skewed Partitioning|Skew]]**.

For instance, we could add two-digit random number at the beginning of the key in order to split the writes evenly across 100 partitions. Though, for reads an additional logic is required as well since we'd need to read the data from 100 partitions.

It only makes sense to **implement** such logic **for specific set of [[Skewed Partitioning|Skewed]] keys**, not for all of them.
