---
aliases:
  - userInput
  - user input
---
`userInput()` — a YQL function that injects user query text into a Vespa query
	safely and with proper tokenization.
 
## How It Works

```
GET /search/?yql=select * from doc where userInput(@q)&q=red shoes
```

1. `@q` is a **reference** to the query parameter `q`
2. Vespa substitutes the value (`"red shoes"`)
3. Applies tokenization, stemming, and match mode based on the field's schema config

## Targeting a Field

`userInput()` is a **predicate generator** — it produces the entire `contains` clause on its own.

```sql
-- WRONG: can't nest inside contains
where title contains userInput(@q)

-- RIGHT: via annotation
where [{"defaultIndex": "title"}]userInput(@q)

-- RIGHT: uses default fieldset from schema
where userInput(@q)
```

## [[Grammar]]

Controls how Vespa parses the user input into query terms.

## Example

```sh
vespa query \
  'yql=select * from msmarco where {defaultIndex:"title", grammar:"all"}userInput(@user-query)' \
  'user-query=red running shoes' \
  'hits=3' \
  'language=en'
```

## See Also

- [[Fieldset]]
- [[Match Mode]]
- [[Matching]]
