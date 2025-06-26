Solutions to [[Write Skew]]:
- **Automatic** write skew prevention requires **[[Serializable]]**;
- **DB constraints** that enforce consistency (e.g. [[PostgreSQL]] Exclude checks);
- **[[Explicit locking]]** on the rows the transaction depend on;
- **[[Materializing conflicts]]** - last resort if transaction depends on absence of rows and is not related to any entity that could be locked (or not possible to be locked under circumstances).
