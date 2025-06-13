**Leaderless** replication - **each replica accepts writes**, either the application itself or coordinator node sends data to replicas.

There's **no such thing as [[Leader failure - failover|failover]]** in leaderless systems. It is possible to [[Writing to leaderless database when some nodes are down|serve requests while some nodes are down]].

See [[Detecting concurrent writes]].