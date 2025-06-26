Scaling the read requests makes fully **synchronous replication almost unusable**, because single node outage would lead to completely blocked writes.

![[Eventual consistency#^7a648b]]

Issues with replication lag:
- [[Reading your own writes]];
- [[Monotonic reads]];
- [[Consistent prefix reads]].

### Solutions for Replication Lag

It should be anticipated how system has to operate when the replication lag is couple of minutes (possibly, hours). If the [[Eventual consistency]] is enough, - that's great. If not, it would make sense to implement [[Reading your own writes|read-after-write]] strategy.

Though, sorting out replication issues on application code level is really complex and easy to get wrong. It would be much simpler if the database could handle such complexity for us. 

The **transactions** were brought in to simplify the application code development. They are usual for single-node database systems. But for distributed systems, some alternative mechanisms may be used (covered in Chapter 7, 9 and part 3)