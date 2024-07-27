[[MVCC]] **Consistent snapshot** is built following way:
- writes of **running transactions are ignored** (list of active transactions is built beforehand at the beginning of current transaction);
- writes made by **rolled back transactions are ignored**;
- writes made by **transactions with greater txid are ignored** - started after current one;
- all other writes are visible to queries.