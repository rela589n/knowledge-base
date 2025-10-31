**Automatic [[Lost Update]] Prevention**:

When ***updating*** the **row**,
	***modified** by* **concurrent [[Transaction]]**,
**current [[Transaction]]** will ***[[Dirty Write#^1048c2|Wait]]** for* **another *to complete***  and: 
- roll back if it committed;
- continue if rolled back.

Supported by [[PostgreSQL]], [[Oracle]], [[SQL Server]]
in **[[Snapshot Isolation]]** level. ^26e2c6

Not supported by [[MySQL]]. ^8ed4f2

> It *does* ***not* prevent** [[Concurrency Problems]]
> 	*for* **processes** ***longer than* [[Transaction]]**.
> 
> **Example:** 
> Two admins modify price of the product. 
> One sets it to 200, another - to 300.
> 
> Running updates sequentially (w/o any concurrent db [[Transaction]]), the last write wins. 
> 
> Likely we'd want to show one error about already modified price ([[Optimistic Locking]]). 
