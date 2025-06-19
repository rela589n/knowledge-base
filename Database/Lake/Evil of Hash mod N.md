When using [[Hash-based Partitioning|partitioning by the hash of key]], we may be tempted to use `mod` operation **to decide which partition** is appropriate.

This **approach** makes **[[Rebalancing Partitions|rebalancing]] _extremely expensive_**, since if we add a single node, then we'd need to rebalance a lot of data.

That's why when [[Hash-based Partitioning|partitioning by the hash of key]], it's better to **use hash ranges**, though it is also possible to make [[Fixed number of Partitions]] beforehand.
