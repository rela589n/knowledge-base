---
aliases:
  - select for update
  - lock for update
---
When logic can't be sensibly implemented via **[[Atomic write operations]]**, then `SELECT` statement may specify `FOR UPDATE` clause. This will lock rows returned by the query until the end of current transaction, thereby preventing these same rows from being  selected for update, updated, or deleted.

