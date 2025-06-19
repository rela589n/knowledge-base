**Clustered index** - [[Database Indexes|Database Index]] that determines **how data is physically placed** on the disk (sorted in the order of index), therefore there could be **only one such index**.

[[Primary Key]] can be used as [[Clustered Index]], if there is need for the efficient search by [[Primary Key]] (yet, inserts/updates might be not so efficient because of the need to reorganize the data).

Clustered Index can be created **for multiple columns**, yet it should be used wisely, since in that case search by [[Primary Key]] will become ineffective (and would require [[Secondary Index]] for the [[Primary Key]]).

Clustered Index can be used for [[Aggregate]] subordinate entities. If [[Entity]] A has outright ownership over [[Entity]] B, it's reasonable that for [[Entity]] B it isn't so important to find by ID, but finding by parent [[Entity]] A is important, since it's owner. Example: User and UserEvent.

In [[MySQL]] data is clustered index by [[Primary Key]]. Every [[Secondary Index]] has the [[Primary Key]] rather than pointer to the location in heap file. ^5263c5

[[PostgreSQL]] does **not** cluster anything automatically. For [[Primary Key]] it creates a unique [[BTree]] so that it can be searched, and [[Secondary Index|Secondary Indexes]] also point to the location on disk. To **cluster the table** (reorganize the order), there's dedicated `CLUSTER` table command that can be used. ^950260

When clustering table, you need to free up the space on disk for at least twice size of the table and indexes, because `CLUSTER` temporarily copies them. Also, after clustering it's recommended to run [[PostgreSQL ANALYSE|ANALYSE]].

`CLUSTER` acquires exclusive table lock, preventing both reads and writes, so be careful. One can check out `pg_repack` for clustering w/o lock.

