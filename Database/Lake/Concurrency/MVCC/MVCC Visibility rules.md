[[MVCC]] **Consistent [[Snapshot Isolation|Snapshot]]** is built following way:
- writes made by **rolled back [[Transaction|Transactions]] *are* ignored**;
- writes made by **[[Transaction|Transactions]] with greater txid *are* ignored** - these started after current one;
- writes of **not committed [[Transaction|Transactions]] are ignored** 
	(list of active [[Transaction|Transactions]] is built beforehand at the beginning of the current [[Transaction]]);
- all **other writes** *are* **visible** to queries (these are either current transaction writes, or ones committed before the current transaction).
