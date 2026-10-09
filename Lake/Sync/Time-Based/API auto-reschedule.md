
Feed query:
```sql
SELECT e.*, p.position
FROM entities e
LEFT JOIN entity_refresh_at r
       ON r.entity_id = e.id AND r.client_id = :clientId
CROSS JOIN LATERAL (SELECT GREATEST(e.updated_at, r.refresh_at) AS position) p
WHERE (p.position, e.id) > (:cursorPosition, :cursorId)
  AND e.deleted_at IS NULL
  AND p.position <= now() - interval '30 seconds'
ORDER BY p.position, e.id
LIMIT :limit;
```

> `now() - interval '30 seconds'` can be configured as `:visibleUntil`.

This query paginates the cursor data over:
- `updated_at` entity timestamp;
- `refresh_at` refresh metadata timestamp.

Thus, If API already knows that after some time ` = refresh_at` the data becomes stale, it can mark this data for re-return, and the query will pick it up.

For each returned page of data, `GET` endpoint will have to set `= refresh_at` synchronization parameter:

```sql
INSERT INTO entity_refresh_at (id, entity_type, client_id, entity_id, refresh_at)
SELECT gen_random_uuid(), :entityType, :clientId, id, now() + interval '70 days' + (random() * interval '14 days')
FROM unnest(:servedEntityIds::uuid[]) AS id
ON CONFLICT (entity_type, client_id, entity_id) DO UPDATE SET refresh_at = EXCLUDED.refresh_at;
```
