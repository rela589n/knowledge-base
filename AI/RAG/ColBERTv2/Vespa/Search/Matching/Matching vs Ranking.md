---
aliases:
  - Match and Rank
---
**Matching vs Ranking** - two separate sequential phases in Vespa query execution.

## Matching

**Goal**: find documents that satisfy query constraints.

- Boolean logic (AND, OR, NOT)
- Filters, range checks
- Uses indexes for speed
- Result: candidate set (no scores)

## Ranking

**Goal**: order candidates by relevance.

- Evaluates [[Rank Profile]] expressions
- Computes scores from rank features
- Multi-phase refinement
- Result: ordered list

## Flow

```
10M docs → [Match] → 50K candidates → [Rank] → Top 10 results
```

## Why Separate?

Efficiency through division of labor:

| Phase | Purpose | Cost |
|-------|---------|------|
| Matching | Elimination — discard fast | Cheap (index lookups) |
| Ranking | Evaluation — score survivors | Expensive (ML models) |

Scoring documents that would be filtered out anyway = wasted compute.
