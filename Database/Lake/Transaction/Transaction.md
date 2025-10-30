---
aliases:
  - Transactions
---
**Transaction** - *sequence of* **reads** *and* **writes**, 
*forming* a **logical unit** 
that's **committed [[Atomicity|Atomically]]**. 

Useful both for:
- [[Single-Object Write]]
- [[Multi-Object Transaction]]

Provides **[[ACID|Safety Guarantees]]** (depending on [[Transaction Isolation Level|Isolation Levels]]) 
	*allowing to* ***pretend** that* some **faults *don't exist*** (abort):
- **app** or **db** ***crashes*** *in the midst of* **writes**:
	- **reboots**, deployments, power outages;
	- **disk** crashes;
- **network *interrupts***;
- [[Concurrency]] problems:
	- clients ***overwriting* changes** of each other;
	- ***reading* partially updated data** ([[Dirty Read]]);
- other **race condition bugs**.

See:
- [[Dirty Read]]
- [[Dirty Write]]
- [[Lost Update]]
- [[Read Skew]]
- [[Write Skew]]

It's possible that **client sent commit** operation, but **TCP connection was interrupted** at this time. Accordingly, client **can't know** whether transaction was **committed or not**.

### Single-Object and Multi-Object operations

#### Handling Errors and Aborts

In **[[Leaderless Replication]]**, it is **up to application to recover** from errors.

The whole point of **[[Transaction]] aborts** is to **allow safe retries**. 
Yet, most ORMs does not retry at all and throw away user input, showing the error message.

Pitfalls of retried transactions:
- if **[[Transaction]] was not ACK-ed** to client, but it was actually executed, then retry **may write data twice** unless app **deduplicate**s it;
- if [[Transaction]] aborted because **DB is overloaded**, retry is **even  worse**. One may **limit the number of retries**, use **[[Exponential backoff]]**, try to **handle** overload-related issues **separately**; 
- **retry won't help** to solve **non-recoverable issues** (**constraint violations**); **retry may help** for **transient issues** like deadlocks, failover, network interruptions, isolation violations;
- some **third-party systems** may **receive multiple (or none) messages** instead of one. **[[Two-phase commit]]** may help to avoid it;
- after couple retries **client may fail** itself, which will mean not written data.

## Summary

--Transactions are the **abstraction**, which allows us to **pretend that some faults do not exist**. Many of the errors come to simple [[Transaction]] abort.

**Without [[Transaction|Transactions]]** process, power, disk, network, concurrency **issues lead to inconsistencies** in the DB. For instance, keeping up to date denormalized data.

Race conditions, which different isolation levels prevent:
- [[Dirty Read|Dirty Reads]];
- [[Dirty Write|Dirty Writes]] (always prevented);
- [[Read Skew]] (**nonrepeatable read**) - [[Transaction]] sees **different parts of the database** in **different points of time**. This is prevented in **snapshot isolation** with **MVCC**.
- [[Lost Update]] - two [[Transaction|Transactions]] use **read-modify-write** cycle leading to changes of one to be overwritten. Some DBs detect lost updates in **snapshot isolation**, while for others **explicit lock** to be used.
- [[Write Skew]] - [[Transaction]] **reads something** (premise), **makes decision** based on it and **performs write**, which leads to **oudated premise** of another transaction. Only **snapshot isolation** prevents it.
- **phantom reads** - **[[Transaction]] searches rows** matching the condition. **Another** transaction **performs the write**, which **affects the result set** of search. **Snapshot isolation** prevents it by means of **index-range locks** which may not be as fine-grained as necessary.

**[[Serializable]]** protects against all race conditions:
- **serial execution** - may be used if write throughput is low and each transaction is fast to execute;
- **two-phase locking** - uses locks, unreliable performance, first concurrent serializable isolation level implementation;
- **serializable snapshot isolation** - uses optimistic lock approach, transactions execute in parallel, on commit serializability is checked and if not satisfied transaction is aborted.

