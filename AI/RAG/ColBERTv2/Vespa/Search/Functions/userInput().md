---
aliases:
  - userInput
  - user input
---
`userInput()` — injects user input into a Vespa YQL query
	safely, with tokenization and configurable parsing.

## Argument

The argument is either:
- a **string literal** — `userInput("red shoes")`
- a **parameter reference** — `userInput(@q)`, where `q` is a query parameter

## How It Works

```
GET /search/?yql=select * from doc where userInput(@q)&q=red shoes
```

1. `@q` references the query parameter `q`
2. Vespa substitutes the value (`"red shoes"`)
3. Applies tokenization, stemming, and match mode based on the field's schema config

## Annotations

| Annotation     | Type    | Default                     | Description                                                     |
| -------------- | ------- | --------------------------- | --------------------------------------------------------------- |
| [[Grammar]]    | string  | `"weakAnd"`                 | How input is parsed.                                            |
| `defaultIndex` | string  | default schema [[Fieldset]] | Field or fieldset to search                                     |
| `allowEmpty`   | boolean | `false`                     | If `true`, empty input matches all documents instead of failing |
## Example

```sh
vespa query \
  'yql=select * from msmarco where {defaultIndex:"title", grammar:"all"}userInput(@user-query)' \
  'user-query=red running shoes' \
  'hits=3' \
  'language=en'
```


### Targeting a Field

`userInput()` is a **predicate generator** — it produces the entire `contains` clause on its own.

```sql
-- WRONG: can't nest inside contains
where title contains userInput(@q)

-- RIGHT: via annotation
where [{"defaultIndex": "title"}]userInput(@q)

-- RIGHT: uses default fieldset from schema
where userInput(@q)
```

## See Also

- [[userQuery()]]
- [[Fieldset]]
- [[Match Mode]]
- [[Matching]]
