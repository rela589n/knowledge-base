---
docs: https://www.postgresql.org/docs/current/indexes-index-only-scans.html
---
Index, that can answer query without the need for [[Table Heap|Heap]] access. 

It can be used only when all the requested query columns are stored in the index.

It uses [[Table Visibility Map]] to avoid [[MVCC Visibility rules|MVCC Visibility Checks]] that require [[Table Heap|Heap]] access.
