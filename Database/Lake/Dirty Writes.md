**Dirty write** - when concurrent **transaction overwrites just written record**. [[Read Comitted]] isolation level prevents this. Usually this is **solved by delaying the write** of a concurrent client until the end of the first transaction.

Reasons to **[[Prevent dirty writes]]**:
- if some statements have **temporal coupling** for both transactions, second transaction may overwrite the value for one statement, while first transaction will overwrite the value for another statement of a second transaction, therefore **leading to the invalid state** (e.g. owner is set to Alice, while invoice is created for Bob);
- if some statements must **accumulate one on another** (like counter increments), some [[Lost Updates|updates may be lost]] (e.g. incremented only once).