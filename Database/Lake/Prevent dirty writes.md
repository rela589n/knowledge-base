Implemented in [[Read Comitted]] isolation level.

To **prevent [[Dirty Writes]]**, **row-level locks** are used. To write the record, database locks row, and **keeps the lock until the end of transaction**. Any other transactions will wait until the lock is released.