---
aliases:
  - Dirty Writes
---
**Dirty Write** - one **[[Transaction]] *overwrites* uncommitted changes of another concurrent [[Transaction]]** (just written). 

**Reasons *to prevent*** it:
- at the end of two [[Multi-Object Transaction]]s, some updates will have succeeded from T1, some from T2 - corrupted state
  (e.g. buying the `car`: update `buyer_id` and `invoice`'s `recipient_id` -  [[Dirty Write - Car example.png|buyer is Alice, yet invoice is for Bob]]);
- statements that ***accumulate* one *on* another** will lead to [[Lost Update]] (e.g. counter incremented only once).

**Solved in [[Read Committed]] 
*by* *delaying*** the concurrent **write** (row-level lock) 
*until* the **end *of*** the [[Transaction]]. ^1048c2

When concurrent [[Transaction]]'s trying to write, 
the database holds the ***lock*** **until *the* end *of* [[Transaction]]**,
thus we'll have to wait.
