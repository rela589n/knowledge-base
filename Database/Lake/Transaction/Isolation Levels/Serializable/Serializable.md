---
aliases:
  - Serializability
---
**Serializable** [[Transaction Isolation Level|Isolation Level]] guarantees that 
*even though* **[[Transaction|Transactions]] may run in parallel**, 
*the* final **result** *would be* ***as if*** they ***ran* serially**. 

Serializability **protects against [[Write Skew]]**.

**Techniques to implement**:
- [[Actual Serial Execution|Actually execute Serially]];
- [[Two-Phase Locking (2PL)]];
- [[Serializable Snapshot Isolation (SSI)]].
