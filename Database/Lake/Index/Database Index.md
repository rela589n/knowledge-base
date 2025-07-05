---
aliases:
  - Index
  - Database Indexes
  - Indexes
---
The idea behind [[Database Index|Indexes]] is to keep some **meta information on the side**, which is like signpost (pointer) to the data we want.

Maintaining additional data structures incurs **write overhead**. When data is inserted, all the **[[Database Index|Indexes]] have to be updated**. It is important trade-off between write and read performance.

Index types:
- [[BTree]]
- [[GIST Index]]
- [[GIN Index]]
- [[BRIN Index]]

[[Unique Index]]

[[Partial Index]]
[[Composite Index]]
[[Expression-based Index]]
[[Covering Index]]
