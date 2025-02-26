**Dirty read** - when concurrent **transaction sees uncommitted changes**. This is prevented in [[Read Committed]] isolation level.

Reasons to **prevent dirty reads**:
- if some statements have **[[Temporal Coupling|temporal coupling]]**, another transaction may see the **database in an invalid state** and take wrong decisions;
- if transaction **rolls back**, and another client **depends on rolled back changes**, this will lead to mind-blowing consequences, since the outcome depends on what has never actually happened.

To **prevent Dirty Reads**, there are two approaches: ^add579
1. (_not used_) briefly **acquire the write lock before reading** the row and **release it right away** after reading. This has the performance penalty since incoming reads wait for some write transactions to commit;
2. [[MVCC]] - database **keeps both old and new values**. While concurrent transaction is **not committed yet**, the **old value is returned**. **On commit** transactions **switch to the new value**. ^d421eb
