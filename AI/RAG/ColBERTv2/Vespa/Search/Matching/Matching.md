---
aliases:
  - Field Matching
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

**[[Indexing Attribute field|attribute]]** — stores value directly in memory
```
"The cat is running" → "the cat is running"
                              ↓
                    Stored as single unit
                    (only lowercased)
```

---

### Processing Pipeline

For example, `indexing: index` and `match: text`:

| Step          | Input                | Output               |
| ------------- | -------------------- | -------------------- |
| Tokenization  | `"Hello-World"`      | `["Hello", "World"]` |
| Lowercasing   | `["Hello", "World"]` | `["hello", "world"]` |
| Normalization | `["café"]`           | `["cafe"]`           |
| Stemming      | `["running"]`        | `["run"]`            |

All steps applied to **both** document and query.

## See Also

- [[Matching vs Ranking]]
- [[Indexing Configuration]]
- [[Indexing Attribute field]]

And also: [[WAND]], [[dotProduct()]]
