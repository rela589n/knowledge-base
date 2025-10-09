---
aliases:
  - MySQL vs PostgreSQL
  - pg vs my
---
##### Clusterization

![[Clustered Index#^950260]]

![[Clustered Index#^5263c5]]

Physically, that's a difference:
- **[[PostgreSQL]]** always inserts data to the **end [[Page]]**;
- while **[[MySQL]]** keeps up **[[Clustered Index]]**.

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

###### Types:

In [[PostgreSQL]] there are [[GIN Index]], [[GIST Index]], [[BRIN Index]] besides standard [[B-Tree]] and [[Hash Index]].

In [[MySQL]] it only [[B-Tree]] and [[Hash Index]] are available.

###### Covering:

In [[PostgreSQL]] there's direct **support for [[Covering Index]]**.

In [[MySQL]] you can only **use [[Composite Index|Multi-column Index]]** to do the same, but it **won't be [[Unique Index]]** on the first column anymore.

###### Expression idx:

Both [[PostgreSQL]] and [[MySQL]] support [[Expression-based Index|Index for Expression]].

##### Schema changes

In [[PostgreSQL]] Schema changes are **[[Transaction|Transactional]]**;

In [[MySQL]] they aren't.

##### Replication

[[PostgreSQL]] uses [[Write-ahead Log (WAL)-based Replication]] by default (yet, alternatives are possible)

[[MySQL]] uses [[Logical (row-based) log Replication]]

##### Connections

[[PostgreSQL]] uses **Process per Connection** (must use IPC).

[[MySQL]] uses **Thread per Connection** (more lightweight).

Thus, [[MySQL]] can handle more concurrent connections (up to 10k in case of Uber), while for [[PostgreSQL]] it's necessary to keep connection [pools](https://wiki.postgresql.org/wiki/Number_Of_Database_Connections?uclick_id=c4efc6bf-8b8a-4e96-9cfa-df99c2ae86dd).

##### Vacuum approaches

[[PostgreSQL VACUUM]] runs full table scan to find deleted rows.

[[MySQL]] uses separate [[Rollback Segment]], where the data is already at hand.

##### Sequences

In **[[PostgreSQL]] sequence** is a separate thing that can be used as is.

In **[[MySQL]]** it seems to be only **AUTO_INCREMENT**, and it's not designed to use it as a separate thing.

##### Table Inheritance

[[PostgreSQL Table Inheritance]] (very, very limited)

[[MySQL]] doesn't support table inheritance.
