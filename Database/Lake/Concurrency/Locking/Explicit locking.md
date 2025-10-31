---
aliases:
  - SELECT FOR UPDATE
  - LOCK FOR UPDATE
---
**SELECT FOR UPDATE** ***locks** the* **returned rows**
	until the **end *of* [[Transaction]]**, 
thereby ***preventing*** these same ***rows*** 
	*from* being ***selected for* update***, updated, or deleted.

It explicitly fixes [[Lost Update]] problem.