When you have a lot of entities (for example, 16), there would be as many joined rows as there are tables (16). This is inefficient if condition by type isn't applied. When type condition is applied, the respective table is tried to be joined only in case of that type.

```sql
LEFT JOIN single_variant_answers
          ON answers.id = single_variant_answers.id
               AND answers.type = '{$singleVariantType}'
LEFT JOIN few_variants_answers
          ON answers.id = few_variants_answers.id
               AND answers.type = '{$fewVariantsType}'
LEFT JOIN few_variants_selected_answers
          ON few_variants_answers.id = few_variants_selected_answers.few_variants_answer_id
               AND answers.type = '{$fewVariantsType}'
```
