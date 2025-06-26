---
aliases:
  - Non-Repeatable Read
---
**Non-repeatable read** (**Read skew**) - situation when **during single transaction** at the end of the transaction some queried records were already changed (if the **same record was to be queried once again, it would come up in a different state**). 

This is prevented in [[Snapshot Isolation]] level.

It could be even more subtle when two **rows are bound one to another**, and we read **first before the change**, and **second after the change**. 

For example, during money transfer between accounts - **first account looks like if it has never received the money** (it was read while transfer transaction had not been committed yet), while **second is as if money were already subtracted from it** (it was read after successful transaction). This makes user think that money vanished into the air.

The **read skew is not acceptable**:
- **for backups** - if restored, the **inconsistencies will become permanent** (like lost money on the balance);
- for **integrity checks**, **analytic queries** - usually scan over a large set of database records; seeing **database in different points of time** will result in **nonsensical results**.
