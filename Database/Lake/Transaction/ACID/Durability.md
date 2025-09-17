**Durability** - database guarantee that **once [[Transaction]] is committed**, it's **committed** and will hold value so that later on we'd be able to **read the written data** regardless of crashes.

In the **[[Replication|Replicated]] databases durability** means that **write** was successfully **processed by W nodes**.

## Replication and Durability

There's no silver bullet for providing a full durability:
- if **machine fails**, we would need to either repair the machine or to **move the disk to another** machine;
- if **code has a bug**, then it will lead to **correlated fault** and no writes will be persisted;
- if using **async replication**, the leader may fail and **recent writes will be lost**;
- if **power is cut off**, **SSD** may not save the data;
- after crashes **files on disk may be corrupted**;
- data may **get corrupted over time** without it being detected;
- within first 4 years, **SSD**s start to have **bad blocks**;
- **HDD**s have high rate of **complete failure**;
- if **SSD is disconnected from power**, it may start **losing the data** within few weeks.
