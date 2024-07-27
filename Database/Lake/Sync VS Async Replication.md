Usually, the **replication is quite fast** - *within a second*. However in some cases (network issues, failure recovery, max load) **followers might fall behind** by several minutes.

Sync replication:
- **pros**: the **follower** is guaranteed to be **up-to-date** with the leader. If the leader suddenly fails, all the master data is still available on the follower
- **con**: if the **follower doesn't respond** (crashed, network issue, etc) the write can not be processed.

**Semi-syncronous configuration**. In practice, if replication is made sync, it means that only **one follower is sync**. In case if it becomes slow, one of the async followers is made sync. This guarantees up-to-date data on **at least two nodes**. 

Often the leader-based replication is made **completely asyncronous**. In this case, **writes are not guaranteed**, because if leader fails, any of it's followers may become leader.
Main reason for doing this is that **leader** may **process writes** even if all of **followers** have **fallen behind**.

>  **Research on Replication**
>  To not lose data if leader fails, and still have good performance and availability, **chain replication** may be used.
>  **Consensus** (getting several nodes to agree on value) has strong connection to consistency.
