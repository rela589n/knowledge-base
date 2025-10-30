---
aliases:
  - WAL
---
**Write-Ahead [[Log (sequence)|Log]]** (WAL) - written **before every modification** of [[B-Tree]].  

Used to accomplish **failover**:
	after crash DB uses WAL is **to [[Consistency|Restore]]** itself.
