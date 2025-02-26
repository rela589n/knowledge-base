**Dirty write** - when concurrent **transaction overwrites just written record**. [[Read Committed]] isolation level prevents this. 

Reasons to prevent dirty writes:
- if transaction issues multiple updates (for example, buying the car updates `buyer_id` and invoice `recipient_id`), then at the end of two concurrent transactions, some updates would be succeeded from transaction 1, and some - from transaction 2 (e.g. [[Dirty Write - Car example.png|owner is set to Alice, while invoice is created for Bob]]), leading to the corrupted state;
- if some statements must **accumulate one on another** (like counter increments), the [[Lost Updates|updates will be lost]] (e.g. incremented only once).

[[Dirty Writes]] are **solved by delaying the write** (row-level lock) of a concurrent transaction until the end of the first transaction. ^1048c2

When the record is written, database **locks the row**, and **keeps it until the end of transaction**. Any other transactions that want to write data will wait until the lock is released.