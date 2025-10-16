---
aliases:
  - Dirty Writes
---
**Dirty Write** - one **[[Transaction]] *overwrites* uncommitted changes of another concurrent [[Transaction]]** (just written). 

[[Read Committed]] prevents this. 

**Reasons *to prevent*** it:
- if transaction issues multiple updates (for example, buying the car updates `buyer_id` and invoice `recipient_id`), then at the end of two concurrent transactions, some updates would be succeeded from transaction 1, and some - from transaction 2 (e.g. [[Dirty Write - Car example.png|owner is set to Alice, while invoice is created for Bob]]), leading to the corrupted state;
- if some statements must **accumulate one on another** (like counter increments), the [[Lost Update|updates will be lost]] (e.g. incremented only once).

[[Dirty Write|Dirty Writes]] are **solved by** 
***delaying*** the **write** (row-level lock) 
	of a concurrent [[Transaction]] 
*until* the **end *of*** the **first** [[Transaction]]. ^1048c2

When writing the record, 
database ***locks*** *the* **row**, 
	and keeps it **until *the* end *of* [[Transaction]]**. 
All other [[Transaction|Transactions]] trying to write the data 
	will wait until the lock is released.
	