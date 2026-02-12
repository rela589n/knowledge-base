---
aliases:
  - match-features
---
A [[Rank Profile]] directive that returns specified [[Rank Features]] alongside with each hit.

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
- **ML training data** — export scoring signals for learning-to-rank

## Match-features vs summary-features

| | `match-features` | `summary-features` |
|---|---|---|
| Computed for | **All** matched hits (first-phase) | Only the **final** returned hits |
| Cost | Higher (runs on every candidate) | Lower (runs on top N) |

