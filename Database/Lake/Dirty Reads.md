**Dirty read** - when concurrent **transaction sees uncommitted writes**. This is prevented in [[Read Comitted]] isolation level.

Reasons to **prevent dirty reads**:
- if some statements have **temporal coupling**, another transaction may see the **database in an invalid state** and take wrong decisions;
- if transation **rolls back**, and another client **depends on rolled back changes**, this will lead to mind-blowing consequences.
