---
aliases:
  - WAL
---
To accomplish **failover**, the **write-ahead log** (WAL) is written **before every modification** of [[BTree]]. After crash this log is **used to restore DB** to a consistent state.
