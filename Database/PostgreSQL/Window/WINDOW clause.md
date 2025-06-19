To avoid duplicating `OVER (...)` in multiple places, you can use `WINDOW` clause to define it once and then specify it in `OVER`.

```sql
SELECT DISTINCT
    order_id,
    FIRST_VALUE(timestamp) over w as created_dt,
    LAST_VALUE(timestamp) over w as last_update_dt,
    LAST_VALUE(action) over w as last_action
FROM events as x
WINDOW w as (PARTITION BY order_id ORDER BY timestamp ASC)
```
