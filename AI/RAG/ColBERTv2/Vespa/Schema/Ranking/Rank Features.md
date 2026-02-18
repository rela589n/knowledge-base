---
aliases:
  - rank features
---
Built-in scoring features.

Pick which ones to expose in responses via [[Match Features]].

## Categories

| Category | Examples | Purpose |
|---|---|---|
| Rank scores | `bm25(field)`, `nativeRank(field)` | Pre-computed relevance scores |
| Field match | `fieldMatch(field).proximity`, `.completeness` | How well query matches a field |
| Attribute match | `attributeMatch(field)` | Match quality for attribute fields |
| Query | `term(n).significance`, `term(n).weight` | Information about query terms |
| Document | `fieldLength(field)`, `attribute(field)` | Document-level signals |
| Geo | `distance(field)`, `closeness(field)` | Geographic distance ranking |
| Global | `now`, `random` | System-level values |

## Commonly used

- `bm25(field)` — good default for first-phase ranking
- `nativeRank(field)` — Vespa's default if no ranking specified
- `fieldMatch(field)` — detailed text match quality
- `closeness(field)` — for nearest neighbor / geo search
- `attribute(field)` — raw attribute value in ranking expressions

[Full catalog](https://docs.vespa.ai/en/reference/ranking/rank-features.html)
