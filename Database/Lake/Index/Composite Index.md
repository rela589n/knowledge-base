---
aliases:
  - Multi-column Index
---
Best practice for **ordering columns** in composite index **is by [[Cardinality|Selectivity]]**, since less index [[Page|Pages]] will be needed to be scanned.

The most common type is **concatenated index**. Columns are concatenated to make a single key. Index, consisting of (firstname+lastname) may be used to find records either by firstname or by both firstname and lastname.

The **part of index to be scanned** is determined by the **leftmost columns** that use **equality operator** (+ **first following column**'s condition).

> **Example:**
> `WHERE a = 5 AND b >= 6 AND c < 77` - index scan will begin from `a = 5, b = 6` up through the last item of `a = 5`;

If you need to **search by any range of columns**, multi-column [[GIN Index]] or [[BRIN Index]] can be used. They provide the same performance regardless of set of columns. 

Also note about [[Bitmap Index Scan|Index Combination Feature]] that uses multiple separate indexes, combining their results.
