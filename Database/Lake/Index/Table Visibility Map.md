---
docs: https://www.postgresql.org/docs/current/indexes-index-only-scans.html
---
**Visibility Map** **makes [[Covering Index]] possible** to use in respect with **[[MVCC Visibility rules]]** without resorting to [[Table Heap|Heap]] access.

It maintains **bit for each [[Page]]** of the table, indicating that it's old enough to be **visible to all current and future [[Transaction|Transactions]]**.

In most situations **it's cached in memory**.
