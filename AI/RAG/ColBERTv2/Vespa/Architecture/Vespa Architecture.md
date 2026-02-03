Vespa is a distributed system.

Even a single-node runs multiple internal services:
- [[Config Server]] (manages configuration)
- [[Container Cluster]] (handles queries)
- [[Content Cluster]] (stores data)
- [[Cluster Controller (health)]] (monitors health, publishes cluster state)
