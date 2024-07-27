**MVCC** (Multi-version concurrency control) - [[Snapshot isolation|snapshot isolation technique]], by which **writes use locks** the same way **as in [[Read Comitted|read committed]]** isolation, and to serve the reads, records **besides of the data hold the id of transactions** (txid) which wrote this data. Id txid is an incremental integer.

The records contain `created_by` and `deleted_by` fields for each row. When the row is updated it is the same as previous version was deleted and new created, iow `update=delete+create`.

The MVCC allows the DB to **observe a consistent snapshot via  [[MVCC Visibility rules|visibility rules]]**.