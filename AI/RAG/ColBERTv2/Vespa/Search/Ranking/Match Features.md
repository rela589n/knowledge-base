---
aliases:
  - match-features
---
A [[Ranking]] directive that returns specified [[Rank Features]] along with each hit.

```vespa
rank-profile my-profile {
    first-phase {
        expression: bm25(title) + bm25(body)
    }
    match-features {
        bm25(title)
        bm25(body)
        nativeRank(title)
        fieldMatch(title).proximity
    }
}
```

## Purpose

- **Debugging** — see why a document ranked the way it did
- **ML training data** — export scoring signals for [learning-to-rank](https://docs.vespa.ai/en/learn/tutorials/text-search-ml)
- **Avoiding fill round-trip** — returned with the first response, unlike [[Summary Features]]

## vs summary-features

In a distributed setup, `summary-features` require a second `.fill()` request:

```
Query → content nodes return top hits (match-features)
      → .fill() fetches summaries (summary-features)
```

|                   | `match-features`                  | `summary-features`               |
| ----------------- | --------------------------------- | -------------------------------- |
| Returned with     | First response from content nodes | Second `.fill()` request         |
| Extra round-trips | None                              | 1                                |
| Risk              | None                              | Documents can move between nodes |

**Real-world case** ([Vinted](https://vinted.engineering/2025/11/06/vespa-match-features/)):
50+ schemas, 500M+ updates/hour — documents redistributed constantly.

Between query and `.fill()`, documents could move to different 
nodes → latency spikes.

Switching to `match-features` dropped P99 from ~9ms to ~3ms.