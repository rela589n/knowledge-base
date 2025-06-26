---
aliases:
  - MySQL vs PostgreSQL
---
##### Clustered Index

![[Clustered Index#^950260]]

![[Clustered Index#^5263c5]]

Physically, that's a difference - [[PostgreSQL]] always inserts data to the end [[Page]], while [[MySQL]] keeps up [[Clustered Index]].

##### Exclude Constraints

[[PostgreSQL Exclude Constraint]]

[[MySQL]] doesn't have exclude constraints.

##### Deferred Check

[[PostgreSQL]] supports [[Deferrable Constraint]]

[[MySQL]] don't.

##### Table Inheritance

[[PostgreSQL Table Inheritance]]

[[MySQL]] doesn't support table inheritance.

##### Replication

[[PostgreSQL]] uses [[Write-ahead log (WAL) shipping]]

[[MySQL]] uses ?