---
aliases:
  - Heap-Only Tuple
---
https://www.postgresql.org/docs/current/storage-hot.html

HOT update is possible only **if update doesn't touch any [[Database Index|Indexed]] fields**, or if **their values aren't changed**.
