---
aliases:
  - Partition Split
  - Rebalancing
---
**Rebalancing** - migrating data and moving load from one node to another.

Necessary when:
- **query throughput** increases;
- **data amount** increases;
- **machine fails** - other need to take over.

 **Requirements** for rebalancing: ^fa9a1b
- the **bare minimum of data** has to be moved for **fast rebalancing**;
- **during the rebalancing** system has to **accept reads and writes**;
- **after rebalancing** the **load should be fairly shared** between nodes.

In spite of [[Partitions Rebalancing#^fa9a1b|Rebalancing Requirements]] , there are multiple strategies to manage nodes and partitions:
- [[Evil of Hash mod N]];
- [[Fixed number of Partitions]];
- [[Dynamic partitioning]];
- [[Partitioning Proportionally to Nodes]].

Rebalancing can be [[Automatic vs Manual Rebalancing]].
