
```sql
SELECT main_entity.id,
       main_entity.name,
       joined_entity.id AS joined_entity_id
FROM main_entity
    LEFT JOIN joined_entity 
        ON joined_entity.id = (
            SELECT first_joined_entity.id
             FROM joined_entity AS first_joined_entity
             WHERE first_joined_entity.main_entity_id = main_entity.id
             ORDER BY first_joined_entity.id DESC
             LIMIT 1
        );
```

See [[DQL Join First Record]]
