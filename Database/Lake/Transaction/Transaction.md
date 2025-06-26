---
aliases:
  - Transactions
---
**Transaction** - sequence of **reads and writes** which make up a **logical unit** and should be **committed [[Atomicity|atomically]]**. It provides **safety guarantees** so that we can **ignore** some **error scenarios** and **concurrency issues**.

Things that can go wrong:
- **database crash** in the mid of write operation;
- **application crash** in the mid of writes;
- **network interrupts** between app and db or db nodes;
- **clients overwrite changes** of each other;
- **partially updated data is read**;
- other **race condition bugs**.

[[Transactions - Poor Performance?]]

Some apps might not need transactions, and for better performance transactional guarantees may be weakened or disabled completely. 

## The Slippery Concept of a Transaction

![[NoSQL - no Transactions#^21bd59]]

### The Meaning of ACID

See [[ACID]].

### Single-Object and Multi-Object operations

**Multi-object transactions** - transactions, which **modify multiple objects** (rows, records, documents). They are especially necessary **if data must be kept in sync** (say, denormalized counter for some query).

The **violation of an isolation** is when on the **halfway of the transaction**, some **other client reads just written data**. **Reading of not committed writes** is known as [[Dirty Read|dirty read]].

To group statements, `START TRANSACTION` and `COMMIT` commands are used. It's possible that **client sent commit** operation, but **TCP connection was interrupted** at this time. Client **can't know** whether transaction was **committed or not**.

#### Single-Object Writes

**Single-object writes** may face **issues the mid of large content upload**:
- the **network is interrupted** or **power fails** - not to store partially inserted/replaced value (**_Atomicity_**). It is implemented using **[[Write-ahead Log-based Replication|WAL]]**;
- **another client** tries to **read** the **same record** - not to show spliced up record (**_Isolation_**). It is implemented using **locks on objects** - only one thread has an access;

> How does it work with transactions? If we modify content in current transation and in the mid of upload server interrupts. How does other clients not see corrupted data? 
> The answer is that MVCC updates are equivalent to delete and create operations. Hence, old value is kept not being overwritten. New value will be abandoned because write didn't commit.

DB support **atomic operations** (like **increments**) to avoid **read-modify-write** cycle, which is **prone to the issue of lost updates**.

**Compare-and-set** may be used to **prevent update** of the **concurrently modified record**.

#### The need for Multi-Object Transactions

**Multi-Object transactions** are **must-have** for most applications.
Conceptually nothing prevents us from distributed transactions implementation, though it is not supported now.

Issues in **not having multi-object transactions**:
1. when inserting **records which reference** one another using **foreign keys**, the data gets out of sync in the mid of writes;
2. since **document databases** encourage **denormalization**, the same **data** need to be **updated in multiple places**, this may get our data out of sync;
3. **secondary indexes** are separately standing storages, which are necessary to be **kept up-to-date with main data**. If actual record was written, but index was not yet updated, then query using this index will not read the record.

#### Handling Errors and Aborts

In **leaderless replication**, it is **up to application to recover** from errors.

The whole point of **transaction aborts** is to **allow safe retries**. Though, this is a pity that some ORM libraries does not retry at all and just throw away user input and show the error message.

Pitfalls of retried transactions:
- if **transaction was not ACK-ed** to client, but it was actually executed, then retry **may write data twice** unless app **deduplicate**s it;
- if transaction aborted because **DB is overloaded**, retry is **even  worse**. One may **limit the number of retries**, use **exponential backoff**, try to **handle** overload-related issues **separately**; 
- **retry won't help** to solve **non-recoverable issues** (**constraint violations**); **retry may help** for **transient issues** like deadlocks, failover, network interruptions, isolation violations;
- some **third-party systems** may **receive multiple (or none) messages** instead of one. **Two-phase commit** (**2PC**) may help to avoid it;
- after couple retries **client may fail** itself, which will mean not written data.

## Weak Isolation Levels

^2864e8

See [[Transaction Isolation Level]]

### Preventing Lost Updates

[[Lost Update]]

### Write Skew and Phantoms

[[Write Skew]]

## Summary

Transactions are the **abstraction**, which allows us to **pretend that some faults do not exist**. A lot of errors come to simple transaction abort.

**Without transactions** process, power, disk, network, concurrency **issues lead to inconsistencies** in the DB. For instance, keeping up to date denormalized data.

Race conditions, which different isolation levels prevent:
- [[Dirty Read|Dirty Reads]];
- [[Dirty Write|Dirty Writes]] (always prevented);
- [[Read Skew]] (**nonrepeatable read**) - transaction sees **different parts of the database** in **different points of time**. This is prevented in **snapshot isolation** with **MVCC**.
- **lost updates** - two transactions use **read-modify-write** cycle leading to changes of one to be overwritten. Some DBs detect lost updates in **snapshot isolation**, while for others **explicit lock** to be used.
- **write skew** - transaction **reads something** (premise), **makes decision** based on it and **performs write**, which leads to **oudated premise** of another transaction. Only **snapshot isolation** prevents it.
- **phantom reads** - **transaction searches rows** matching the condition. **Another** transaction **performs the write**, which **affects the result set** of search. **Snapshot isolation** prevents it by means of **index-range locks** which may not be as fine-grained as necessary.

**Serializable isolation level** protects against all race conditions:
- **serial execution** - may be used if write throughput is low and each transaction is fast to execute;
- **two-phase locking** - uses locks, unreliable performance, first concurrent serializable isolation level implementation;
- **serializable snapshot isolation** - uses optimistic lock approach, transactions execute in parallel, on commit serializability is checked and if not satisfied transaction is aborted.

