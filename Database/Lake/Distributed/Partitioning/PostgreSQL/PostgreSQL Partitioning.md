---
docs:
  - https://habr.com/ru/companies/quadcode/articles/679618/
---
[[Partitioning Test]]

Create partition (list):

```sql
CREATE TABLE user_login_events PARTITION OF user_events
    FOR VALUES IN ('id1', 'id2');
```

[[Foreign Key]] toward the Partitioned table creates [[Inherited Constraint]] for every partition:

![[PostgreSQL Partitioning Foreign Key.png]]

