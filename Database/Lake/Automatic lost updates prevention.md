PostgreSQL, Oracle, Sql Server support automatic lost update detection when running in **[[Snapshot isolation]]** level. MySQL doesn't detect lost updates automatically.

If there were **concurrent transaction**, which **modified the same row as the current transaction**, DB will **roll back the current transaction** and throw an error.

If the current transaction is trying to modify the same row as another transaction has already modified, the current transaction will wait until the concurrent transaction either rolls back (in that case, current transaction's update will complete), or commits (in that case, current transaction throws serialization error).

