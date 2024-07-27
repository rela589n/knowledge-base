In [[Read Comitted]] isolation level to **prevent [[Dirty Reads]]**, there are two approaches:
1. (_not used_) briefly **acquire the write lock before reading** the row and **release it right away** after reading. This has the performance penalty since incoming reads wait for some write transactions to commit;
2. database may **keep both old and new values**. While concurrent transaction is **not committed yet**, **old value is returned**. **After commit** transactions **switch to the new value**. See [[MVCC]].
