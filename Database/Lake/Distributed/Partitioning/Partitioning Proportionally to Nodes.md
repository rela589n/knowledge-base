This approach is used in: [[Cassandra]] , [[Ketama]]

With both [[Dynamic partitioning]] and having [[Fixed number of Partitions]], the **number of nodes** and **number of partitions** are independent.

**Proportional partitioning** - the way to [[Partitioning|Partition]] the data so that a **static number of [[Partition|Partitions]] per node** is kept. Applicable to **[[Hash-based Partitioning]] only**.

The existing **partitions grow along with the dataset**. Once they can't grow anymore, we **add more nodes**, and **existing partitions become smaller** again. When adding new node **system randomly selects N** (number of partitions per node) **existing partitions**, splits them and **migrates the half of the data** to the new node.
