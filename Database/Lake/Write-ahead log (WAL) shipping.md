As the WAL is anyway written to the disk (in LSM-trees and B-Trees), we may send it to the followers as well. Used in Postgres, Oracle.

The problem is that **WALs are low level** (like which bytes were changed in which disk blocks), which makes replication coupled to the storage engine. 

When it is necessary to **upgrade database version**, there are two cases:
- the newer version of storage engine on replicas can't accept old format. In this case upgrade **would require downtime (BC break)**;
- the newer version of storage engine on replicas may accept old WAL format. In this case it is necessary to upgrade all followers first. It can be done **without downtime (BC retained)**.
