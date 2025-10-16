**Unsync clocks** won't cause dramatic crash. Instead it will be **subtle data loss**. Software needs to be **prepared for incorrect clocks**.

If **precise clocks are required** for the code, it is necessary to have the **clocks monitoring** on nodes in cluster and **once clock is too far away**, declare the **node dead** and remove from the cluster.

Issues with unsync clocks:
- [[Timestamps for ordering events - data loss]];
- [[Clock confidence interval]];
- [[Synchronized clocks for global snapshots]].

