---
docs:
  - https://docs.vespa.ai/en/reference/querying/simple-query-language.html
---
Search syntax for user, parsed by [[userQuery()]].

## Operators

| Operator | Meaning | Example |
|---|---|---|
| `term` | match term (AND by default) | `red shoes` → both required |
| `+term` | must match | `+red shoes` → `red` required |
| `-term` | must not match | `red -shoes` → exclude `shoes` |
| `"phrase"` | exact phrase | `"red shoes"` |
| `field:term` | field-scoped search | `title:shoes` |
| `term*` | prefix wildcard | `sho*` |
| `[min;max]` | numeric range | `[10;50]` |
| `(a b)` | grouping | `(red blue) shoes` |

## Examples

```
red shoes               # both terms required
red -leather shoes      # no leather
"running shoes"         # exact phrase
title:shoes             # search title field only
sho*                    # prefix match
[10;50]                 # range
```

## Notes

- NOT used by [[userInput()]] — that function uses the `grammar` annotation instead
- Behavior is fixed — no grammar configuration
