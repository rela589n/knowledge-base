**Single-Object Writes** are 

**Issues** (<u>large content</u>):
- **network interrupts** / **power fails** - partially saved/updated value ([[Atomicity]]). Fixed with **[[Write-ahead Log (WAL)-based Replication|WAL]]**;
- **other client** *is **reading*** the **same record** - spliced up (if no [[Isolation]]). 
  Fixed with **locks on objects** - only one thread has an access;

> How does it work with [[Transaction|Transactions]]? 
> If we modify content in current [[Transaction]] and in the mid of upload server interrupts. How clients do not see corrupted data?
> Answer: [[MVCC]] updates are equivalent to delete and create operations. Hence, old value is kept not being overwritten. New value will be abandoned because write didn't commit.

DB support **[[Atomic write operations]]** (like **increments**) to avoid **[[Read-Modify-Write]]** cycle, which is **prone to the issue of [[Lost Update|Lost Updates]]**.

**[[Compare-and-Set]]** may be used to **prevent update** of the **concurrently modified record**.

