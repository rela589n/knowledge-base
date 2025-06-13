---
aliases:
  - Serializability
---
**Serializable** isolation level guarantees that even though **transactions may run in parallel**, the final **result** would be **as if they ran serially**. Serializability **protects against [[Write Skews]]**.

**Techniques to implement** serializability:
- literally execute transactions **[[Actual Serial Execution|serially]]**;
- [[Two-Phase Locking (2PL)]];
- [[Serializable Snapshot Isolation (SSI)]].
