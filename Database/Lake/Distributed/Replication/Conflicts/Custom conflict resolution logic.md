The databases usually provide a way to customize the resolution logic. It may be either **on write** or **on read**.

- **on write** - [[Bucardo|PostgreSQL Bucardo]]. When conflict is detected from replication stream, **custom code is executed**.
- **on read** - [[CouchDB]]. All the **conflicting writes are stored**. Later on, when data is read, the application can **show user the conflicting data** and let him decide what to do with it.

> Conflicts relate to individual rows (not to the transaction).

##### Automatic conflict resolution
- Conflict-free replicated **data types** ([[Conflict-free Replicated Data Types|CRDTs]]) - sets, maps, ordered lists, counters etc. **can be concurrently edited**. Can be used in **any topology**;
- **Mergeable persistent data structures** - track all changes explicitly, use three-way merge strategy (compared to [[Conflict-free Replicated Data Types|CRDTs]] which use 2-way merge);
- **Operational transformation** - used in Etherpad, Google Docs. Specifically for ordered lists of items. The reliable algorithms require **central server**.
