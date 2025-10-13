---
docs: https://www.postgresql.org/docs/current/indexes-index-only-scans.html
aliases:
  - Include Index
---
**Covering [[Database Index|Index]]** can **answer queries without [[Table Heap|Heap]] access**.

It can be used only when **all requested columns** are **stored in the [[Database Index|Index]]**.

It uses [[Table Visibility Map]] to avoid [[MVCC Visibility rules|MVCC Visibility Checks]] that require [[Table Heap|Heap]] access. Thus, it's only reasonable if [[Page|Pages]] aren't modified frequently.

[[Primary Key]] can also be `INCLUDED` with other columns.

[[Composite Index|Multi-column Index]] can be [[Covering Index]] by itself.

