Most common way to end up with same data on all replicas is **leader-based  replication** (aka, **active/passive**, **master-slave**):
1. **leader** (master, primary) replica is the first who accepts **write operations**;
2. **followers** (slaves, secondaries, hot standbys) - replicas, which use the **change stream** (repliation log) from *leader* in order **to update local data**;
3. **writes** are served only **by leader**, whereas **reads** may be served either **by leader or followers**.

Support:
- relational: [[PostgreSQL]], [[Oracle]], [[MySQL]], [[SQL Server]];
- non-relational: [[MongoDB]], [[RethinkDB]], [[Espresso]];
- message-brokers: [[Kafka]], [[RabbitMQ]] - for highly-available queues.

More:
- [[Setting up new Followers]] with no downtime;
- [[Handling node outages]];
- [[Leader lease]].
