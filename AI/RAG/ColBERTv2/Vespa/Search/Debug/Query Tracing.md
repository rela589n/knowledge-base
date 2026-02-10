---
aliases:
  - trace.level
  - Query Trace
---
Debugs query execution by revealing the internal query structure after processing.

## How to Enable

Add `trace.level` to your query request:

```sh
vespa query \
  'yql=select * from doc where userInput(@user-query) and url contains ({filter:true,ranked:false}"news.url.com")' \
  'user-query=red running shoes' \
  'trace.level=3' \
  'language=en'
```

Add `trace.timestamps=true` for timing info per searcher invoked.

## Trace Levels

| Level | Shows                                              |
| ----- | -------------------------------------------------- |
| 1     | Basic trace output                                 |
| 2     | Search chain components (query pre-processing)     |
| 3     | Query transformations, term rewrites               |
| 4+    | All components invoked in the query, their ordering |

## What to Look For

Example trace output:
```
query=[AND (WEAKAND(100) default:red default:run default:shoe) |url:'news url com']
```

This reveals:
- **Operator conversions** — `userInput` became `WEAKAND`
- **Stemming** — `running` → `run`, `shoes` → `shoe`
- **Field scoping** — terms prefixed with field name (`default:`)
- **Tokenization effects** — `news.url.com` → `news url com`
- **Unranked terms** — `|` prefix indicates `ranked: false`

## Custom Tracing

In application code, use `Query.trace` to add custom trace output.

## See Also

- [[Vespa Debugging]]
- [[Grammar]]
- [[Vespa Query Annotations - ranked and filter]]
