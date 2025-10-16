[[VoltDB]] , [[Redis]], #Datomic, #H-Store

Reasons to rethink actual serial execution:
- RAM is cheap, some **DBs keep everything in memory**;
- In most cases **OLTP transactions are short**, while OLAP are usually readonly and can operate on snapshot isolation level.

#### Encapsulating transactions in stored procedures

The **interactive style** of transactions leverages **network** a lot (requests, responses). If we allow only one transaction to run in one point of time, this would lead to **dreadful performance**.

Another approach is to use **stored procedure** and make the **DB aware of all steps of the transaction** beforehand. Even though transactions are executed one by one they don't wait for the application to submit the next query, hence **performance is NOT limited by network** anymore, also we don't have the concurrency control overhead and locks. If  the **dataset is completely in memory**, we'll have **no disk IO overhead**. This allows us to have pretty good performance in single-threaded environments.

#### Pros and cons of stored procedures

**Bad reputation** of stored procedures:
- each vendor uses it's **own language** to write them. This is not a general-purpose language, no libraries are available;
- **maintenance is harder** - hard to debug, tricky to test, need to deploy, harder to maintain in VCS, monitoring and metrics collection is not possible;
- **instance performance** - multiple app instances may connect to the single database. While app scaling is relatively simpler, DB scaling is much more harder. Therefore, **poorly written** code in **procedure** leads to **worse outcome** compared to the same poor app code.

Though, **some DBs** now **use general-purpose languages** ([[VoltDB]] uses Java and Groovy, Datomic uses Java and Clojure, [[Redis]] uses Lua).

#### Partitioning

For apps with **high write throughput** a **single-threaded [[Transaction|Transactions]]** processor may be a **serious bottleneck**.

Write throughput may be **scaled to multiple CPUs** if it is possible for application to partition the data in the way so that **transactions operate within the partition boundaries**.

In VoltDB it is also possible to run **cross-partition transactions**. Though, it's write throughput is quite limited and can't be scaled, as well as it is a lot **slower compared to single-partition transaction**.

#### Summary of serial execution

Actual serial execution is viable with remarks:
- every **[[Transaction]] must be lightning-fast** (no network communication, everything through stored procedure);
- **active data set must fit in memory**. Some rarely-used data may be backed up on disk, but when it's necessary again, **anti-caching** approach should be used - roll back transaction, fetch data in memory, restart the transaction;
- **write throughput** must be **low enough** to be handled by single CPU, **otherwise partitioning is necessary** to be used with the requirement of no cross-partition transaction;
- **cross-partition [[Transaction|Transactions]] are possible** as well, though require DB coordination and are substantially slower compared to single-partition tansactions.
