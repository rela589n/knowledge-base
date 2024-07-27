**Rebalancing** - migrating data and moving load from one node to another.

Necessary when:
- **query throughput** increases;
- **data amount** increases;
- **machine fails** - other need to take over.

Rebalancing **requirements**:
- the **bare minimum of data** has to be moved for **fast rebalancing**;
- **during the rebalancing** system has to **accept reads and writes**;
- **after rebalancing** the **load should be fairly shared** between nodes.

See [[Automatic vs Manual Rebalancing]].

