PostgreSQL, Oracle, Sql Server support automatic lost update detection when running in **[[Snapshot isolation]]** level. MySQL doesn't detect lost updates automatically.

If there were **concurrent transaction**, which **modified the same row as we**, DB will **roll back current transaction** and throw an error.

If current transaction is trying to modify the same row as another transaction has already modified, current transaction will wait until concurrent transaction either rolls back (in that case, current transaction's update will complete), or commits (in that case, serialization error is thrown in current transaction).

