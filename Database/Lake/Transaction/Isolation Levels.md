---
aliases:
  - Transaction Isolation Levels
  - isolation level
---
Race conditions arise when users access the same (or dependent) database rows. 

**Transaction isolation** was meant to **hide concurrency issues** from devs. 

**[[Serializable]]** level means that any **transactions** are executed **as if they were serial**, though it was rarely used because of 
**high performance penalty** (in case of [[MySQL]]), and can be used with [[PostgreSQL]] if configured retries.

Levels:
- Read Uncomitted (not used);
- [[Read Committed]];
- [[Snapshot isolation]];
- [[Serializable]].
