**MVCC** (Multi-version concurrency control) - [[Snapshot Isolation|snapshot isolation technique]], in which **[[Dirty Writes#^1048c2|writes use locks]]** the same way **as in [[Read Committed|read committed]]** isolation, and to serve the reads, the database **records**, besides the actual data, **hold the id of transactions** (txid) which wrote this data. Id txid is an incremental integer.

The records contain `created_by` (txid) and `deleted_by` (txid) fields for each row. When the row is updated it is the same as if the previous version was deleted and new created, iow `update=delete+create`.

The MVCC allows the DB to **observe a consistent snapshot via  [[MVCC Visibility rules|visibility rules]]**.