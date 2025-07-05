---
aliases:
  - Index on Function
  - Expression-based Index
---
**[[Database Index|Index]] on Expression** makes it possible to create **[[Database Index|Index]] for a complex expression** so that it will be **considered as query plan** so that there'd be **no need for manual computation** at runtime (**no [[Sequence Scan]]**).

```sql
CREATE INDEX test_col1_lower_idx ON test (lower(col1));
```

This query will not compute it again, and [[BTree]] will make the access fast:
```sql
SELECT * FROM test WHERE lower(col1) = 'value';
```

It's worth mentioning that non-[[HOT update]]s must maintain every index, and therefore value is recomputed.

Note that [[Index on Expression|Expression-based Indexes]] re-evaluate expression every time [[HOT update]] happens ([[Hot Update Test]]).