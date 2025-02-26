**Snapshot isolation** (**repeatable read**) - [[Isolation Levels|Transaction Isolation Level]], that provides a guarantee of seeing the consistent snapshot during the whole lifespan of the transaction. The **transaction sees** rows in the state committed at **the beginning** of the transaction.

It prevents [[Read skews]].
In [[PostgreSQL]], it also prevents [[Automatic lost updates prevention|Lost Updates]].

See [[Implementing Snapshot Isolation]] for internal details.

> ?? How does it all work if we don't wrap reads into a transaction. I assume each operation is a separate transaction, and it is no different from [[Read Committed]]?

## Snapshot isolation and naming confusion

**[[Snapshot isolation|Snapshot isolation]]** is called **serializable** in Oracle and **Repeatable Read** in PostgreSQL and MySQL. In IBM DB2 **Repeatable Read** refers to **[[Serializable|serializability]]**.
