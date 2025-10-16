---
aliases:
  - Transaction Isolation Levels
  - Isolation Level
---
**Transaction Isolation** is meant to **hide concurrency issues** from devs.

Race conditions arise when users access the same (or dependent) database rows.

**[[Serializable]]** level means that [[Transaction|Transactions]] are executed 
*as if* **they *were* serial**.

It's rarely used in [[MySQL]] due to **high performance penalty**.
It can be used with [[PostgreSQL]] if configured **retries**.

Levels:
- Read Uncomitted (not used);
- [[Read Committed]];
- [[Snapshot Isolation]];
- [[Serializable]].
