Are 1-indexed.

```sql
SELECT
       ar.ar[3] -- outputs 7
FROM (SELECT ARRAY[5,6,7] ar) ar;
```
