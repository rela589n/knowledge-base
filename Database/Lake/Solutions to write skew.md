Solutions to [[Write Skews]]:
- **Automatic** write skew prevention requires **[[Serializable]]**;
- **DB constraints** that enforce consistency (e.g. PostgreSQL Exclude checks);
- **explicit lock** on rows the transaction depend on;
- [[Materializing conflicts]] - last resort if transaction depends on absence of rows.
