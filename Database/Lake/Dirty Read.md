---
aliases:
  - Dirty Reads
---
**Dirty read** - when **one [[Transaction]] sees uncommitted changes of another [[Transaction]]**. Prevented in [[Read Committed]].

Reasons to **prevent [[Dirty Read|Dirty Reads]]**:
- if some statements have **[[Temporal Coupling]]**, another transaction may see the **database in an invalid state** and take wrong decisions;
- if [[Transaction]] **rolls back**, and another client **depends on rolled back changes**, this will lead to mind-blowing consequences, since the outcome depends on what has never actually happened.

Ways to **Prevent [[Dirty Read|Dirty Reads]]**: ^add579
1. (_not used_) briefly **acquire the write lock before reading** the row and then **release it right away**. This has the performance penalty since the incoming reads will have to wait for write transactions to commit;
2. [[MVCC]] - database **keeps both old and new values**. While concurrent transaction is **not committed yet**, the **old value is returned**. **On commit switch to the new value**. ^d421eb
