---
aliases:
  - Repeatable Read
---
**Snapshot isolation** - [[Transaction Isolation Level|Transaction Isolation Level]], that provides a guarantee of seeing the **consistent snapshot** during the **whole lifespan** of the [[Transaction]]. Select statements returns committed rows in their state at **the beginning** of the [[Transaction]].

It prevents [[Read skews]].
In [[PostgreSQL]], it also prevents [[Automatic Lost Updates prevention|Lost Updates]].

See [[Implementing Snapshot Isolation]] for internal details.

> ?? How does it all work if we don't wrap reads into a transaction. I assume each operation is a separate transaction, and it is no different from [[Read Committed]]?

## Snapshot isolation and naming confusion

**[[Snapshot Isolation|Snapshot Isolation]]** is called **serializable** in [[Oracle]] and **Repeatable Read** in [[PostgreSQL]] and [[MySQL]]. In IBM DB2 **Repeatable Read** refers to **[[Serializable|Serializability]]**.
