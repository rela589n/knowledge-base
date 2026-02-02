---
aliases: []
---
Vespa's `:` operator behaves differently depending on field type.

## `index` field — text search

```
verse_text:beginning
```

- Matches "In the beginning God created..."
- Case-insensitive
- Stems words ("running" matches "run")
- More like "contains token" than "equals"

## `attribute` field — exact match

```
chapter_num:5
```

- Matches exactly `5`
- Closer to SQL `=`

## Comparison

| Query Type       | SQL               | Vespa (index) | Vespa (attribute) |
| ---------------- | ----------------- | ------------- | ----------------- |
| Exact match      | `= 'Genesis'`     | ❌            | ✅ `:`            |
| Contains token   | `LIKE '%word%'`   | ✅ `:`        | ❌                |
| Full-text search | external engine   | ✅ `:`        | ❌                |

## Exact string match on text

If you need exact match on a text field:
- Use `attribute` instead of `index`
- Or use `word` match mode in schema
