---
aliases:
  - VACUUM
---
Since [[PostgreSQL]] uses [[MVCC]] model for concurrency control, updated/deleted rows are still kept under their unused versions.

In order to reclaim this space for usage by database/operating system, `VACUUM` operation could be used.

> [[PostgreSQL]] runs `VACUUM` automatically, when `autovacuum` feature is enabled.

Plain `VACUUM` - reclaims the space, and makes it available for use within the same table (doesn't give space away to OS). It doesn't require exclusive lock, thus reads and writes may continue to work.

`VACUUM FULL` - rewrites the full content of the table into the new file, allowing OS to reuse freed up space. It requires ACCESS EXCLUSIVE lock on the table, being processed.

See also [[PostgreSQL ANALYSE|ANALYSE]]