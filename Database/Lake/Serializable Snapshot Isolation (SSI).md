SSI has small performance penalty compared to [[Snapshot isolation]]

#### Pessimistic vs Optimistic concurrency control

[[Pessimistic concurrency control]]

[[Optimistic concurrency control]]

**Serializable Snapshot Isolation (SSI)** - [[Optimistic concurrency control]] method, **based on snapshot isolation level**, which **adds** logic of **serialization anomalies detection** at the transaction commit time, and if there are any, **aborts some transactions**.

#### Decisions based on outdated premise

The transaction queries may have causal dependency (e.g. writes depend on the read data).

**Outdated Premise** - statement that was true at the beginning of transaction, but no longer true at the commit time.

Cases to **detect** possibly **outdated premises**:
- **reading stale MVCC objects** (there were uncommitted writes before read);
- **writes that affect premise** (the write was published after read).

**If on *commit time* there are any *outdated premises* related to current transaction's read queries, it is aborted.**

#### Detecting stale MVCC reads

When transaction **reads object** from the MVCC table, it may find out that **some not committed writes** from other transactions **are present**. It will **keep track** of these writes **until the commit**. If during the commit it turns out that **writes were committed**, current **transaction is aborted**.

#### Detecting writes that affect prior reads

When transaction **reads the data**, this information is **tracked in index** entries similarly to [[Transactions#Index-range locks|Index-range locks]], hence we can know which data is read by which transaction.

When transaction **writes the data**, it looks at the indexes to **check which transactions have read matching rows**. Then, current transaction **notifies** transactions **about new outdated premise**.

#### Performance of Serializable Snapshot Isolation

As with **Snapshot Isolation**, readers don't block writers and writers don't block readers, therefore **queries latency is predictable**.

The overall **performance** of SSI highly **depends on rate of aborts**. It in turn, **depends** on internal implementation of **transactions activity bookkeeping**. The more **precise** it is, the **less chance of** unnecessary **abort** is, but it **adds its own overhead**. 

As a rule of thumb, **SSI transactions should not be long-running**, because in case of abort it would take some time to retry. SSI is less sensitive to slow transactions compared to 2PL or serial execution.
