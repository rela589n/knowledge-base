---
aliases:
  - Dirty Reads
---
**Dirty Read** - one **[[Transaction]]** *sees* **uncommitted changes** 
	***of* another [[Transaction]]**.  
Solved by [[Read Committed]].

**Reasons *to prevent***:
- if **one** [[Transaction]] ***rolls back***, 
  then **another**  ***depends on***  **rolled back changes**, this will lead to mind-blowing consequences, since the outcome depends on what has never actually happened;
- if statements are subject to **[[Temporal Coupling]]**, 
  another **[[Transaction]]** may ***see*** the **database** ***in*** an **invalid state** 
  and take wrong decisions.

Ways to **Prevent [[Dirty Read|Dirty Reads]]**: ^add579
1. (_not used_) briefly ***acquire***  **write lock**  ***before* reading** the row 
	   and then **release it right away**. 
   It has a **performance penalty** 
	   since the incoming **reads** will have to ***wait*** *for* **write** [[Transaction|Transactions]] ***to commit***;
2. [[MVCC]] - ***keep*** both **old** *and* **new** values. 
   While concurrent [[Transaction]] is **not committed yet**, 
	   **old value** is returned. 
   On **commit** - database
	   returns **new value**. ^d421eb
