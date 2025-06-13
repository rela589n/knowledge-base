**Clustered index** - [[Database Indexes|Database Index]] that determines **how data is physically placed** on the disk (sorted in the order of index), therefore there could be **only one such index**.

Usually [[Primary Key]] is used as [[Clustered Index]], and so that search by [[Primary Key]] is very efficient (though, inserts/updates might be not so efficient because of the need to reorganize the data).

Clustered Index can be created for multiple columns, yet it should be used wisely, since in that case search by [[Primary Key]] could become ineffective (and would require [[Secondary Index]] for that [[Primary Key]]).

In [[MySQL]] data is clustered index by [[Primary Key]]. Every [[Secondary Index]] has the [[Primary Key]] rather than pointer to the location in heap file. ^5263c5

In [[PostgreSQL]] data is **not** automatically clustered by [[Primary Key]]. Instead, [[PostgreSQL]] creates a unique [[BTree index]] for [[Primary Key]], and thus [[Secondary Index|Secondary Indexes]] point to the location on disk. To **cluster the table**, there's dedicated `CLUSTER` table command that can be used. ^950260

