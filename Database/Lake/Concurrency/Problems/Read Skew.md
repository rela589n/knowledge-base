---
aliases:
  - Non-Repeatable Read
  - Read Skews
---
**Read skew** (Non-repeatable read) - situation when 
*at the* ***end*** ***of** the* **[[Transaction]]**
some **queried records** *are* **already changed** 
	(if we were to ***query** the* **same record** *once **again***, 
	 it would be in a **different state**).

This is prevented in [[Snapshot Isolation]] level.

It could be even more **subtle** 
	when two **rows** *are* ***bound***  **one *to* another**, 
and we *read*  **first** ***before** the* **change**, 
	and **second** ***after** the* **change**.

> **Example**: Account **Money Transfer**
> 
> **First** ***looks like*** *if* **money** *were* ***never* received**
> 	(had been *read before* transfer [[Transaction]] was committed),
> while **second *as if* money were already subtracted from it** 
> 	(it was read after successful transaction). 
> 	
> This makes user think that money ***vanished** into the* **air**.

Read skew is **not acceptable**:
- **for backups** - if restored, the **inconsistencies will become permanent** (like lost money on the balance);
- for **integrity checks**, **analytic queries** - usually scan over a large set of database records; seeing **database in different points of time** will result in **nonsensical results**.
