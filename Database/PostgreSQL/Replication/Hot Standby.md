**Hot Standby** is the mode in which [[PostgreSQL]] [[Replica|Replicas]] work.

Since it's [[Write-ahead Log (WAL)-based Replication]],
[[Replica|Replicas]] constantly check for new [[Write-Ahead Log|WAL]] records.
In comparison, during normal crash recovery DB doesn't accept accept queries until it fully processed [[Write-Ahead Log|WAL]].
