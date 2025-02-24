---
aliases:
  - read-after-write
---
There may be the case when shortly **after user has submitted** the data, he will **see obsolete information** (not seeing the written data), as the data is retrieved from the replica.

The **read-after-write** (aka, **read-your-writes**) consistency is necessary to sort out this problem:

- read **from the leader** all things that **could've possibly been modified** (current customer profile information as an example);
- if almost every thing could've possibly been modified, the customer **last modification time** may be kept somewhere. Then, **for one minute** after the modification, reads for that customer are **served only by the leader** (relying on [[Eventual consistency]] that should have happened during that minute). Besides that, it is also possible to monitor the replication lag and prevent queries to the not caught up followers;
- the **last modification timestamp** may be kept for every customer. The reads are **served from the caught up at least to this timestamp** replicas. If no replicas can handle the read, then query may wait.

The **cross-device** read-after-write consistency - we want to reflect recent modifications on all customer devices (like web app and mobile):
- the customer **last update timestamp must be centralized**, because one device doesn't know if another had any modifications;
- if replicas reside in different datacenters, there's no guarantee that all devices will be connected to the same datacenter.
