---
aliases:
  - Match Properties
---
**Matching** is the process of determining
  whether a document's field content
  satisfies a query condition.

It happens in **two phases**:
1. **Indexing** — transform and store document content
2. **Querying** — transform query terms and compare against stored content

## How It Works

### The Core Principle

Both document content and query terms
  go through the **same transformations**
  so they can be compared on equal terms.

```
Document: "Running in the Dreams"
              ↓ (transform)
Stored as: ["run", "dream"]

Query: "dreaming"
              ↓ (same transform)
Becomes: "dream"

Match? → Yes ✓
```

---

### Two Indexing Pathways

**`index`** — builds inverted index for full-text search
```
"The cat is running" → ["the", "cat", "is", "run"]
                              ↓
                    Inverted index maps:
                    "run" → [doc1, doc47, doc302...]
```

**`attribute`** — stores value directly in memory
```
"The cat is running" → "the cat is running"
                              ↓
                    Stored as single unit
                    (only lowercased)
```

---

### Processing Pipeline

For example, `indexing: index` and `match: text`:

| Step          | Input              | Output             |
| ------------- | ------------------ | ------------------ |
| Tokenization  | "Hello-World"      | ["Hello", "World"] |
| Lowercasing   | ["Hello", "World"] | ["hello", "world"] |
| Normalization | ["cafe"]           | ["cafe"]           |
| Stemming      | ["running"]        | ["run"]            |

All steps applied to **both** document and query.

---

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
            match: exact # "SKU-123" matches only "SKU-123" (case-insensitive)
        }
    }
}
```

## See Also

- [[Matching vs Ranking]]
- [[Indexing Configuration]]
- [[Indexing Attribute field]]
