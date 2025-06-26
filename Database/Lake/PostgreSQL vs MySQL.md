---
aliases:
  - MySQL vs PostgreSQL
---
##### Clusterization

![[Clustered Index#^950260]]

![[Clustered Index#^5263c5]]

Physically, that's a difference - [[PostgreSQL]] always inserts data to the end [[Page]], while [[MySQL]] keeps up [[Clustered Index]].

When row is updated:
- [[MySQL]] rewrites it in place (old is backed up in [[Rollback Segment]]), and only needed [[Database Indexes|Indexes]] are updated (if there was indexable field update). 
- [[PostgreSQL]] writes new [[MVCC]] version, and it needs to update [[Table Heap|Heap File]] pointers for all the indexes (if [[HOT update]] wasn't used).
##### Exclude Constraints

[[PostgreSQL Exclude Constraint]]

[[MySQL]] doesn't have exclude constraints.

##### Deferred Constraints

[[PostgreSQL]] supports [[Deferrable Constraint|Deferrable Constraints]]

[[MySQL]] doesn't.

##### Table Inheritance

[[PostgreSQL Table Inheritance]] (very, very limited)

[[MySQL]] doesn't support table inheritance.

##### Vacuum approaches

[[PostgreSQL VACUUM]] runs full table scan to find deleted rows.

[[MySQL]] uses [[Rollback Segment]], so the data is already at hand.
##### Replication

[[PostgreSQL]] uses [[Write-ahead Log (WAL)-based Replication]]

[[MySQL]] uses ?