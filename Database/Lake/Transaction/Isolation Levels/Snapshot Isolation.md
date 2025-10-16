---
aliases:
  - Repeatable Read
---
**Snapshot isolation** - [[Transaction Isolation Level|Isolation Level]], that guarantees 
*seeing the* **consistent snapshot** 
	*during the* **whole lifespan** *of the* [[Transaction]].
Select statements return committed **rows** 
in the **state *at the* beginning** *of the* [[Transaction]].

It prevents [[Read Skew]].

In [[PostgreSQL]], it also prevents [[Automatic Lost Updates prevention|Lost Updates]].

See [[Implementing Snapshot Isolation]] for internal details.

#### Naming confusion

**[[Snapshot Isolation|Snapshot Isolation]]** is called **serializable** in [[Oracle]],
**Repeatable Read** in [[PostgreSQL]] and [[MySQL]]. 
	While in IBM DB2 **Repeatable Read** refers to **[[Serializable]]**.
