---
aliases:
  - UOW
---
**Unit of Work** - groups multiple operations to database that must be issued in a [[Transaction]].

It allows to ***track*** changes **in memory**, 
and then ***issue*** all the **bulk** of them 
	in a **single commit** operation.
