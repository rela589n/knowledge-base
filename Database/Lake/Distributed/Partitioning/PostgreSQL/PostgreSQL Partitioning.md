---
docs:
  - https://habr.com/ru/companies/quadcode/articles/679618/
---
[[Partitioning Test|Partitioning Example]], [[Partitioning Task]]

Create partition (list):

```sql
CREATE TABLE user_login_events PARTITION OF user_events
    FOR VALUES IN ('id1', 'id2');
```

> ⚠️ You can't use [[Generated Column]] as Key of Partition.

[[Foreign Key]] toward the Partitioned table creates [[Inherited Constraint]] for every partition:

![[PostgreSQL Partitioning Foreign Key.png]]

