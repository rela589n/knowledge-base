---
aliases:
  - "ranked: false"
  - "filter: true"
docs:
  - https://docs.vespa.ai/en/learn/tutorials/text-search.html#combine-free-text-with-filters
---
Query annotations that control how a term affects ranking and presentation.

## `ranked: false`

- The term does **not** contribute to the relevance score
- Default: `true`

Without it, every matching document gets an artificial score boost
  from the filter term — even though the user didn't search for it.

In practice, when used with AND (all results match the filter),
  the boost is roughly the same across documents,
  so relative ordering barely changes.

Still useful for:
- Performance (Vespa skips score computation for this term)
- Edge cases where BM25 boost is not uniform (varying term frequency or field length)
- Keeping absolute scores clean (for thresholds, logging, cross-query comparison)

## `filter: true`

- The term is **not** used for bolding, highlighting, or dynamic snippeting
- Default: `false`

Without it, the filter value (e.g. a URL) would appear emphasized in result summaries
  — misleading, since the user searched for something else.

## Usage

```yql
select * from doc where
  default contains "search query"
  and url contains ({filter: true, ranked: false}"url")
```

Think of it like a SQL `WHERE` clause — narrows result set,
						invisible to ranking and presentation.
