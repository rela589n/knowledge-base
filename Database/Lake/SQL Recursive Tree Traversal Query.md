Following query implements [[Preorder Tree Traversal]] for sections tree.

1. At first, top sections are selected.
2. Then, on every iteration, inner sections are joined and added to the existing list of sections, building tree path at the same time.
3. Finally, it's all sorted by path and returned.

```sql
WITH RECURSIVE preorder_sections_traversal
                   AS (SELECT section.id,
                              section.parent_id,
                              ARRAY [ROW (section.sort_order,section.id)] AS path
                       FROM questionnaire_sections section
                       WHERE section.parent_id IS NULL
                       UNION ALL
                       SELECT section.id,
                              section.parent_id,
                              preorder_sections_traversal.path || ROW (section.sort_order,section.id) AS path
                       FROM preorder_sections_traversal
                                INNER JOIN questionnaire_sections section
                                           ON preorder_sections_traversal.id = section.parent_id)
SELECT section.*
FROM questionnaire_sections section
         INNER JOIN preorder_sections_traversal tree ON section.id = tree.id
WHERE section.deleted_at IS NULL
ORDER BY tree.path ASC;
```