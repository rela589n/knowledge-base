---
aliases:
  - Index Combination Feature
---
Consider we have a query `WHERE x = 5 AND y = 6`.

If database has one [[Database Index|Index]] on `x`, and another [[Database Index|Index]] on `y`, then two queries can be launched, **each building so-called Bitmap**.

**Bitmap** represents **locations of table rows** in memory. **Bitmaps are then combined** as query needs, and the rows are returned.

Note that any **[[Database Index|Index]] ordering is lost** due to Bitmap. Rows are **returned in physical order**.

[Doc](https://www.postgresql.org/docs/current/indexes-bitmap-scans.html)