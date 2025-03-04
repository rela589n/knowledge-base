---
aliases:
  - Convert time to time zone postgresql
---
It's possible to convert time to the needed time zone:

```sql
SELECT send_at,
(send_at AT TIME ZONE 'Europe/Kiev')::TIME as send_time
FROM messages;
```