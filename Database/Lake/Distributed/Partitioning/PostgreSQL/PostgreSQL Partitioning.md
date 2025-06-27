[[Partitioning Example]]

Create partition (list):

```sql
CREATE TABLE user_login_events PARTITION OF user_events
    FOR VALUES IN ('login');
```
