---
aliases:
  - select for update
---
When logic can't be sensibly implemented via **[[Atomic write operations]]**, then `select` statement may specify `for update`. This will lock all rows returned by the query until current transaction commits, preventing them from being updated, deleted, or selected for update.

