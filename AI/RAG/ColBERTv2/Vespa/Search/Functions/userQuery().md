---
aliases:
  - userQuery
  - user query
---
`userQuery()` — reads from `model.queryString` and parses it with the simple query language.

## Syntax

```sql
select * from doc where userQuery()
```

No argument — always reads from `model.queryString` (set via the `query` HTTP parameter).

## Simple Query Language Behavior

Parsed using [[Simple Query Language]].

- Terms are AND-ed by default ([[model.type]] = `'all'`) — `red AND shoes` → docs must have both
- Prefix `-` negates a term — `red -shoes` → must contain `red`, must not contain `shoes`

## Contrast with `userInput()`

|              | `userQuery()`                 | `userInput()`                                     |
| ------------ | ----------------------------- | ------------------------------------------------- |
| Input source | `model.queryString`           | any query parameter via `@param` or inline string |
| Grammar      | fixed (simple query language) | configurable via `grammar` annotation             |
| Annotations  | none                          | `grammar`, `defaultIndex`, `allowEmpty`           |

## See Also

- [[userInput()]]
- [[Grammar]]
