[[MVCC]] **Consistent [[Snapshot isolation|snapshot]]** is built following way:
- writes of **not committed transactions are ignored** (list of active transactions is built beforehand at the beginning of the current transaction);
- writes made by **rolled back transactions are ignored**;
- writes made by **transactions with greater txid are ignored** - these started after current one;
- all other writes are visible to queries (these are either current transaction writes, or ones committed before the current transaction).