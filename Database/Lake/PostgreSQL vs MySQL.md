---
aliases:
  - MySQL vs PostgreSQL
---
##### Clusterization

![[Clustered Index#^950260]]

![[Clustered Index#^5263c5]]

Physically, that's a difference - [[PostgreSQL]] always inserts data to the end [[Page]], while [[MySQL]] keeps up [[Clustered Index]].

When row is updated:
- [[MySQL]] rewrites it in place (old is backed up in [[Rollback Segment]]), and only needed [[Database Index|Indexes]] are updated (if there was indexable field update). 
- [[PostgreSQL]] writes new [[MVCC]] version, and it needs to update [[Table Heap|Heap File]] pointers for all the indexes (if [[HOT update]] wasn't used).
##### Exclude Constraints

[[PostgreSQL Exclude Constraint]]

[[MySQL]] doesn't have exclude constraints.

##### Deferred Constraints

[[PostgreSQL]] supports [[Deferrable Constraint|Deferrable Constraints]]

[[MySQL]] doesn't.

##### Indexes

In [[PostgreSQL]] there are [[GIN Index]], [[GIST Index]], [[BRIN Index]] besides standard [[BTree]].

In [[MySQL]] it seems that only [[BTree]] is available.

##### Sequences

In [[PostgreSQL]] sequence is a separate thing that can be used as is.

In [[MySQL]] it seems to be only AUTO_INCREMENT, and it's not designed to use it as a separate thing.

##### Replication

[[PostgreSQL]] uses [[Write-ahead Log (WAL)-based Replication]] by default (yet, alternatives are possible)

[[MySQL]] uses [[Logical (row-based) log Replication]]

##### Connections

[[PostgreSQL]] uses **Process per Connection** (must use IPC).

[[MySQL]] uses **Thread per Connection** (more lightweight).

Thus, [[MySQL]] can handle more concurrent connections (up to 10k in case of Uber), while for [[PostgreSQL]] it's necessary to keep connection [pools](https://wiki.postgresql.org/wiki/Number_Of_Database_Connections?uclick_id=c4efc6bf-8b8a-4e96-9cfa-df99c2ae86dd).

##### Schema changes

In [[PostgreSQL]] Schema changes are [[Transition|Transactional]];

In [[MySQL]] they aren't.

##### Vacuum approaches

[[PostgreSQL VACUUM]] runs full table scan to find deleted rows.

[[MySQL]] uses separate [[Rollback Segment]], where the data is already at hand.

##### Table Inheritance

[[PostgreSQL Table Inheritance]] (very, very limited)

[[MySQL]] doesn't support table inheritance.
