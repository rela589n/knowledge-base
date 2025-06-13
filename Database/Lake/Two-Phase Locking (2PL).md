**Two-phase locking** (**2PL**) - approach to provide [[Serializable|Serializability]], which **protects from all kinds of race conditions** including lost updates and write skew. It no longer follow **reads never block writes** and **writes never block reads**. 

Instead reads block writes and vice versa:
- if transaction **A has read object**, and transaction **B wants to write it**, B will have to **wait for A to finish** (no unexpected changes to read objects);
- if transaction **A has wrote object**, and transaction **B wants to read it**, B will have to wait **for A to finish** (reading old versions of object is not acceptable).

#### Implementation of 2PL

Used by [[MySQL]], [[SQL Server]], [[DB2]]

**Shared lock** - does not prevent other transactions from taking this lock on the same rows, but does **prevent taking exclusive lock**.
**Exclusive lock** - **prevents any other transaction from locking** with either Shared or Exclusive lock on the same rows.

Locks are used following way:
- when transaction **reads something**, it acquires **shared lock** on these rows;
- when transaction **writes something**, it acquires **exclusive lock** on these rows;
- if transaction **first reads then writes**, then **shared lock is promoted to exclusive lock** on the modified rows;
- locks are hold until the end of transaction.

**Two-phase locking** means:
- **during transaction** execution, **locks are acquired** (first phase);
- at the **end of transaction** all **locks are released** (second phase).

In some situations **deadlock** may arise, then **one transaction is aborted** (it should be retried by the application), while **other continues** execution.

#### Performance of 2PL

**Concurrency is reduced**. One single small transaction **may wait for a dozen transactions** to complete. It takes only one single large transaction to grind system to halt.
Because of it, **latency is unstable**. At high percentiles 2PL DBs are very slow.
**Locks** itself **introduce overhead**.
**Deadlocks** in 2PL are quite frequent. This brings an **overhead of retrial**.

#### Predicate locks

2PL with no predicate locks is vulnerable to new inserts (phantoms), which will cause write skew. Since non-existing data isn't locked, nothing prevents it from modification of other transaction query result once committed.

**Predicate lock** - **shared lock** on the query **search criteria**. Key idea is that it **applies to objects** which do **not yet exist** in the database. It makes 2PL serializable.

Combined with 2PL predicate locks:
- when data is **read**, **predicate lock is acquired first**. If another transaction holds exclusive lock on any object which matches the predicate, current transaction will have to **wait until writing transaction commits**;
- when data is **modified** (insert, update, delete), the transaction has to **check if** either old or new **value matches any existing predicate locks**. If so, current transaction will have to **wait until predicate lock is released**.

#### Index-range locks

**Index-range locking** (**next key locking**) - **shared lock** is attached **to index entries** during the search. When insert/update/delete trigger **update of index**, transaction will have to **wait for shared lock** to be released. This approach is used in most 2PL implementations **instead of predicate locks**.

This approach is **not that precise** as **predicate locks** are (the index may leverage only one field, while query uses multiple), but it is a good **performance compromise**, since checking all predicate locks during the update takes a lot of time, while **index update is necessary anyway** (if there's index, if no - shared lock is taken on whole table).

> ?? how does index-range locking work when update is triggered by primary key. If the updated field is not used in index, write is supposed to acquire lock anyway. How it will do? Will it scan all existing indexes? Maybe index is only necessary for create and delete, while for update the locks on actual rows are used.
