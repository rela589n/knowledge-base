**Leaderless [[Replication]]** - **each [[Replica]] accepts writes**, either the application itself or coordinator node sends data to replicas.

There's **no such thing as [[Leader failure - Failover|failover]]** in leaderless systems. It is possible to [[Writing to Leaderless database when some nodes are down|serve requests while some nodes are down]].

See [[Detecting concurrent writes]].