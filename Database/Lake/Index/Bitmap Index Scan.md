---
aliases:
  - Index Combination Feature
---
Let's say we have a query `WHERE x = 5 AND y = 6`.

Database has:
- [[Database Index|Index]] on `x`;
- [[Database Index|Index]] on `y`.

Two **queries** can be launched, **each building** so-called **Bitmap**.

**Bitmap** represents **locations of table rows** in memory. 
Then, **bitmaps are combined** as the query needs, 
and the rows are returned.

Note that any **[[Database Index|Index]] ordering is lost** due to Bitmap. 
Rows are returned by their **physical order**.

[Doc](https://www.postgresql.org/docs/current/indexes-bitmap-scans.html)