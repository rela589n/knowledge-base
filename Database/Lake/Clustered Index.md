Clustered index - index that determines how data is physically placed on the disk (sorted in the order of index), therefore there could be only one clustered index.

Usually [[Primary Key]] is used for the [[Clustered Index]], and that's why search by [[Primary Key]] is very efficient (though, inserts/updates might be not so efficient because of the need to reorganize the data).

Clustered Index could be created for multiple columns, yet it should be used wisely, since in that case search by [[Primary Key]] could become ineffective (and would require [[Secondary Index]] for that [[Primary Key]]).

MySQL stores data in clustered index by [[Primary Key]]. Every secondary index has pointer to the [[Primary Key]] rather than location in heap file. ^5263c5

In [[PostgreSQL]] [[Primary Key]] is **not** automatically clustered. Instead, [[PostgreSQL]] creates a unique [[BTree index]] for [[Primary Key]]. To cluster table, a separate `CLUSTER` table command could be used. ^950260

