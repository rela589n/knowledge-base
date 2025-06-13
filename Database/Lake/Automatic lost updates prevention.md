[[PostgreSQL]], [[Oracle]], [[SQL Server]] support automatic [[Lost Updates]] detection  when running in **[[Snapshot Isolation]]** level. 

> [[MySQL]] doesn't detect lost updates automatically.

If there were **concurrent transaction**, which **modified the same row as the current transaction**, DB will **roll back the current transaction** and throw an error.

If current transaction is trying to **modify the same row** as already modified by another transaction, the current transaction will **wait until the concurrent transaction** either commits (in that case, current transaction throws serialization error) or rolls back (in that case, current transaction's update will complete) - this is the same lock mechanism as used to prevent dirty writes ([[Dirty Writes#^1048c2]]).

> It is important to understand that even though lost update is detected on the database level, **this will not prevent from the concurrency problems that *span longer than transaction*** lives. For example, when two admins open product page to modify its price, one setting it to 200, another setting it to 300, then running update sequentially (w/o concurrent db transaction), the last write will win, while we'd expect one to see error message about already modified price. In that case [[Optimistic Locking]] should be used.
