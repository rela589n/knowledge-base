[[Replication Log|Replication Strategy]]

In simplest case, leader **logs every single write statement**, and then sends it to the followers.

This may break if:
- statements use `RAND()` , `NOW()` and similar **functions**;
- statements use **autoincrementing column**, or **depend on existing data** (like `UPDATE WHERE`), they must be executed  **precisely in the same order** on each [[Replica]];
- statements **have side-effects** (triggers, user-defined functions), then each [[Replica]] may have **different side-effects**.

Generally **other [[Replication Log|Replication Strategies]] are preferable**, because there are a lot of edge cases which could not be covered by plain replacement of non-deterministic function-call with static value in the log file.
