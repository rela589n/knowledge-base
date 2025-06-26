[[Replication Strategies|Replication Strategy]], that leverages [[Write-Ahead Log|WAL]], since anyway it's written to the disk (in LSM-trees and [[BTree|BTrees]]), so it can be sent to the [[Replica|Followers]] as well. Used in [[PostgreSQL]], [[Oracle]].

The problem is that **[[Write-Ahead Log|WAL]]s are low level** (like which bytes were changed in which disk blocks), which makes [[Replication]] coupled to the storage engine.

When it is necessary to **upgrade database version**, there are two cases:
- *(good)* the newer version of storage engine on [[Replica|Replicas]] can accept old [[Write-Ahead Log|WAL]] format. In this case it is necessary to upgrade all [[Replica|Followers]] first. It can be done **without downtime (BC retained)**.
- *(bad)* the newer version of storage engine on [[Replica|Replicas]] can't accept old format. In this case upgrade **would require downtime (BC break)**;
