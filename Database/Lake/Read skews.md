**Non-repeatable read** (**Read skew**) - if **during single transaction** the **same record is queried**, it may be **in different states**. It may be even more subtle when two **rows are bound one to another**, and we read **first before the change**, and **second after the change**. This is prevented in [[Snapshot isolation]] level.

For instance, money transfer between accounts - first account looks like if it has never received the money, while second is as if money were subtracted from it. This makes user think that money vanished into the air.

The **read skew is not acceptable**:
- **for backups** - if restored, the **inconsistencies will become permanent** (like lost money on the balance);
- for **integrity checks**, **analytic queries** - usually scan over a large set of database records; seeing **database in different points of time** will result in **nonsensical results**.
