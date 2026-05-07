---
aliases:
  - SQL find overlapping periods
---
```sql
SELECT DISTINCT time_slots.day_id
FROM time_slots
         INNER JOIN time_slots AS time_slots_2
                    ON time_slots.day_id = time_slots_2.day_id
                        AND time_slots.id < time_slots_2.id
                        AND time_slots.start_time < time_slots_2.end_time
                        AND time_slots.end_time > time_slots_2.start_time;
-- 10:00 - 11:00
-- 09:00 - 12:00

-- 10:00 - 11:00
-- 10:59 - 12:00

-- 10:00 - 11:00
-- 09:00 - 10:01
```
