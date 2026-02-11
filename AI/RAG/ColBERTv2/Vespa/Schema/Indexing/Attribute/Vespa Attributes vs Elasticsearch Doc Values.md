Both solve the same problem:
a forward index (doc → value) for sorting, filtering, aggregations.

The difference is **who manages memory**.

## Comparison

|           | Vespa (attribute)                | Elasticsearch (doc values)           |
| --------- | -------------------------------- | ------------------------------------ |
| Storage   | Application manages RAM          | OS filesystem cache                  |
| Hot data  | Always in memory                 | OS decides what to cache             |
| Cold data | Still in memory (unless `paged`) | Naturally evicted to disk            |
| Startup   | Must load everything into RAM    | Just opens files, OS pages on demand |
| OOM risk  | High (2x spike at init)          | Low (OS handles it)                  |
| Latency   | Predictable (always in RAM)      | Depends on cache hits                |

## Design philosophy

- **Vespa**: "we manage memory ourselves for guaranteed speed"
- **Elasticsearch**: "let the OS handle it — good enough for most cases"

## When Elasticsearch approach works well

- Working set fits in available memory → performance close to in-memory
- If it doesn't → graceful degradation, not a crash

## When Vespa approach wins

- <b><u>Latency-critical</u> workloads</b> where page faults are unacceptable
- <b><u>Predictable</u> performance</b> matters more than cost
