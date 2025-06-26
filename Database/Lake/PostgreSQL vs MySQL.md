---
aliases:
  - MySQL vs PostgreSQL
---
##### Clustered Index

![[Clustered Index#^950260]]

![[Clustered Index#^5263c5]]

Physically, that's a difference - [[PostgreSQL]] always inserts data to the end [[Page]], while [[MySQL]] keeps up [[Clustered Index]].

When row is updated, [[MySQL]] uses [[Rollback Segment]], and [[Database Indexes|Indexes]] needn't to be updated if it wasn't indexable field. [[PostgreSQL]] needs to update [[Table Heap|Heap File]] pointers for all indexes (if [[HOT update]] wasn't used).

##### Exclude Constraints

[[PostgreSQL Exclude Constraint]]

[[MySQL]] doesn't have exclude constraints.

##### Deferred Constraints

[[PostgreSQL]] supports [[Deferrable Constraint|Deferrable Constraints]]

[[MySQL]] doesn't.

##### Table Inheritance

[[PostgreSQL Table Inheritance]] (very, very limited)

[[MySQL]] doesn't support table inheritance.

##### Replication

[[PostgreSQL]] uses [[Write-ahead log (WAL) shipping]]

[[MySQL]] uses ?