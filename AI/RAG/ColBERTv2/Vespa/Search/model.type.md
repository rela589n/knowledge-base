---
docs:
  - https://docs.vespa.ai/en/reference/api/query.html#model.type
---
HTTP parameter shorthand that sets how [[userQuery()]]'s `model.queryString` is parsed.

```
/search/?query=red+running+shoes&model.type=all
```

## Parsing Modes

| Mode            | `"red running shoes"` becomes        | Meaning                                          |
| --------------- | ------------------------------------ | ------------------------------------------------ |
| `"weakAnd"`     | `weakAnd(red, running, shoes)`       | Soft AND — prefers all, allows partial (default) |
| `"all"`         | `red AND running AND shoes`          | All words must match                             |
| `"any"`         | `red OR running OR shoes`            | Any word can match                               |
| `"phrase"`      | `"red running shoes"`                | Terms treated as an ordered phrase               |
| `"linguistics"` | linguistics(red, running, shoes)     | Applies stemming and linguistic normalization    |
| `"tokenize"`    | [red, running, shoes] (no operators) | Just splits into tokens                          |
| `"web"`         | web(red, running, shoes)             | Web-style: handles +/- operators                 |
| `"yql"`         | parsed as YQL expression             | Full YQL — input must be valid YQL               |

> The `grammar` annotation on [[userInput()]] uses the same parsing modes.

## Sub-parameters

- `model.type.composite` — how sub-expressions combine
- `model.type.tokenization` — tokenizer to use
- `model.type.syntax` — syntax variant within a mode
