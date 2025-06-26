---
aliases:
  - SELECT FOR UPDATE
  - LOCK FOR UPDATE
---
When [[Lost Update]] can't be sensibly prevented via **[[Atomic write operations]]**, then `SELECT` statement may specify `FOR UPDATE` clause. This will **lock the rows** returned by the query until the **end of the [[Transaction]]**, thereby preventing these same rows from being  selected for update, updated, or deleted.
