---
docs:
  - https://habr.com/ru/companies/quadcode/articles/679618/
  - https://www.postgresql.org/docs/current/sql-cluster.html
aliases:
  - Clusterization
---
**Clustered [[Database Index|Index]]** -  determines how **data** is **physically placed** on disk. The data is sorted by it, therefore it's possible to cluster only by **one such index**.

Primary aim is **efficient search**:
- for **[[Primary Key]]** when if it's the main query pattern (yet, inserts/updates might be not so efficient due to the need to reorganize the data);
- for **subordinate entities** of [[Aggregate]]:
	- If [[Entity]] **A** has **full ownership** over [[Entity]] **B**, 
	  it's reasonable that subsidiary [[Entity]] B isn't needed to be found by ID, but only by parent [[Entity]], since it's owner. Example: User and UserEvent ([[Clustered Index Example]]).

It can be created **for multiple columns**, though it is to be used wisely, because search by [[Primary Key]] might become ineffective (and would require [[Secondary Index]] for the [[Primary Key]]) - in case of [[MySQL]].


**[[MySQL]] always** creates [[Clustered Index]] for [[Primary Key]]. Every [[Secondary Index]] stores [[Primary Key]] (rather than [[Table Heap|Heap File]] pointer) to define the location. ^5263c5

**[[PostgreSQL]]** does **not cluster** anything **automatically**. For [[Primary Key]] it creates a unique [[BTree]] so that it can be searched, and [[Secondary Index|Secondary Indexes]] also point to the location on disk. To **cluster the table** (reorganize the order), there's dedicated `CLUSTER` table command that can be used. ^950260

When clustering table, you need to free up the space on disk for at least twice size of the table and indexes, because `CLUSTER` temporarily copies them. Also, after clustering it's recommended to run [[PostgreSQL ANALYSE|ANALYSE]].

`CLUSTER` acquires exclusive table lock, preventing both reads and writes, so be careful. One can check out `pg_repack` for clustering w/o lock.

