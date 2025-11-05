**Unsync clocks** won't cause dramatic crash, 
but will cause **subtle data loss**:
- [[Timestamps for ordering events - data loss]];
- [[Clock Confidence Interval]];
- [[Synchronized clocks for global snapshots]].

If **precise clocks are required** for the code,
it is necessary to have the **clocks monitoring** 
	on nodes in cluster
and **once clock is too far away**,
	declare the **node dead** and remove it from the cluster.
