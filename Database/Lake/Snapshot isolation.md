**Snapshot isolation** (**repeatable read**) - [[Isolation Levels|Transaction Isolation Level]], in which each **transaction sees** rows in the state they were **committed before the beginning** of the transaction. 

It prevents [[Read skews|non-repeatable reads]]. 
In [[PostgreSQL]], it also prevents [[Automatic lost updates prevention|lost updates]].

See [[Implementing Snapshot Isolation]] for internal details.

> ?? How does it all work if we don't wrap reads into a transaction. I assume each operation is a separate transaction?

## Snapshot isolation and naming confusion

**[[Snapshot isolation|Snapshot isolation]]** is called **serializable** in Oracle and **Repeatable Read** in PostgreSQL and MySQL. In IBM DB2 **Repeatable Read** refers to **[[Serializable|serializability]]**.
