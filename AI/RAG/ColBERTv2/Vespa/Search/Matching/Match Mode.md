**[[Matching]] Mode**.

### Why [[Match Mode]]s Matter

The `match` setting controls **which transformations** apply:

| Match Mode | Tokenize | Lowercase | Normalize | Stem |
|------------|----------|-----------|-----------|------|
| `text`     | ✓        | ✓         | ✓         | ✓    |
| `word`     | ✓        | ✓         | ✗         | ✗    |
| `exact`    | ✗        | ✗         | ✗         | ✗    |

This determines matching flexibility vs. precision:
- `text` — "running" matches "run" (high recall)
- `word` — "running" matches only "running" (exact word)
- `exact` — "Running" ≠ "running" (character-perfect)

---

### Practical Example

```vespa
schema product {
    document product {
        field description type string {
            indexing: index | summary
            match: text # "running shoes" matches query "run shoe"
        }

        field sku type string {
            indexing: attribute | summary
            match: exact # "SKU-123" matches exact "sku-123" (case-insensitive)
        }
    }
}
```
