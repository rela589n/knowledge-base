The users may **update the same entity at the same time on different leaders**. For instance, first user sets title=B, while second sets title=C. Both of them see successful message. Yet, title could be either one or the other.

![[Replication conflicts]]

Write conflicts may be detected in [[Sync vs Async conflict detection|sync or async]] manner.

There are multiple ways to deal with conflicts:
- [[Conflict avoidance]] (recommended);
- [[Converging toward a consistent state]];
- [[Custom conflict resolution logic]].