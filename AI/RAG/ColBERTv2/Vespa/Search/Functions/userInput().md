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

## Grammar

Controls how Vespa parses the user input into query terms.

```
{defaultIndex:"title", grammar:"all"}userInput(@user-query)
```

| Grammar      | `"what is dad bod"` becomes     | Meaning                                          |
| ------------ | ------------------------------- | ------------------------------------------------ |
| `"weakAnd"`  | weakAnd of all terms            | Soft AND — prefers all, allows partial (default)  |
| `"all"`      | `what AND is AND dad AND bod`   | All words must match                             |
| `"any"`      | `what OR is OR dad OR bod`      | Any word can match                               |
| `"tokenize"` | tokenized but no operators      | Just splits into tokens                          |
| `"segment"`  | treats as a single segment      | For CJK / unsegmented languages                  |
| `"raw"`      | `"what is dad bod"` as-is       | No parsing at all                                |

## Example

```sh
vespa query \
  'yql=select * from msmarco where {defaultIndex:"title", grammar:"all"}userInput(@user-query)' \
  'user-query=what is dad bod' \
  'hits=3' \
  'language=en'
```

## See Also

- [[Fieldset]]
- [[Match Mode]]
- [[Matching]]
