**Multi-version [[Concurrency]] Control** (MVCC) - **[[Snapshot Isolation|Repeatable Read]] technique**, in which:
- **[[Dirty Write#^1048c2|writes use locks]]** the same way **as in [[Read Committed|read committed]]** isolation, 
- reads are served this way: each **record**, besides the actual data, **holds incremental id of the [[Transaction]]** (txid), which wrote this data.

The records contain `created_by` (txid) and `deleted_by` (txid) fields for each row. 
When the row is updated it is the same as if the previous version was deleted and new created, iow `update=delete+create`.

The MVCC allows the DB to **observe a consistent snapshot via  [[MVCC Visibility rules|Visibility Rules]]**.