```sql
SELECT DISTINCT value  
FROM UNNEST(ARRAY [  
    'value1',  
    'value2',  
    'value2'  
    ]) AS value
```
