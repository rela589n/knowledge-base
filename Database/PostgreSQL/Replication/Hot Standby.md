**Hot Standby** is the mode in which [[PostgreSQL]] [[Replication|Replicas]] work.

Since it's implemented with [[Write-ahead log (WAL) shipping]], [[Replication|Replicas]] constantly check for the new [[Write-Ahead Log|WAL]] records.
In comparison, during normal crash recovery DB doesn't accept accept queries until fully processed [[Write-Ahead Log|WAL]].
