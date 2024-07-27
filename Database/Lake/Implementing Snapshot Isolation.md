The key principle of snapshot isolation is that **reads never block writes** and **writes never block reads**.

Usually [[Snapshot isolation]] is implemented with [[MVCC]].

## Indexes in Snapshot Isolation

Indexation highly depends on internal implementation.
- the **BTree index** may **point to all versions of rows** and query executor will filter out not visible rows based on txid;
- the **copy-on-write** approach may be used - every write creates a new root of BTree, hence making consistent snapshot, therefore no need to filter the actual rows.
