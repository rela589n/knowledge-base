---
aliases:
  - Multicolumn Index
---
Best practice for **ordering columns** in composite index **is by [[Cardinality|Selectivity]]**, since less index [[Page|Pages]] will be needed to be scanned.

The **part of index to be scanned** is determined by the **leftmost columns** that use **equality operator** (+ **first following column**'s condition).

> **Example:**
> `WHERE a = 5 AND b >= 42 AND c < 77` - index scan will begin from `a = 5, b = 42` up through the last item of `a = 5`;

