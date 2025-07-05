---
docs:
  - https://habr.com/ru/companies/quadcode/articles/679618/
---
[[Partitioning Test]]

Create partition (list):

```sql
CREATE TABLE user_login_events PARTITION OF user_events
    FOR VALUES IN ('login');
```

[[Foreign Key]] toward the Partitioned table creates [[Inherited Constraint]] for every partition:

![[PostgreSQL Partitioning Foreign Key.png]]

