```sql
SELECT word, ndoc  
FROM TS_STAT('select search_vector from table')
ORDER BY ndoc DESC
LIMIT 3;
```