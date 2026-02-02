---
aliases: []
---
**Attribute** field - stores field value **in RAM** as a forward index (document → value).

## Structure

Column-oriented array, not a hash map:

```
Document ID:  [0]       [1]       [2]         [3]
book:         Genesis   Exodus    Leviticus   Numbers
chapter_num:  1         1         1           1
```

- Document ID = array index
- Direct lookup: `doc[2].book` → "Leviticus" (O(1))

## Why array, not hash map?

- More memory-efficient (no key storage overhead)
- Cache-friendly (sequential memory access)
- Document IDs are sequential integers internally

## Enables

- Sorting (`order by book`)
- Filtering (`book = "Genesis"` exact match)
- Grouping (`group by book`)
- Range queries (`chapter_num > 5`)
- Fast access in ranking expressions

## Memory implications

10 million documents × 100-byte attribute ≈ 1 GB RAM

**Options if too large:**

```
field book type string {
    indexing: attribute
    attribute: paged    # memory-mapped file, OS manages RAM
}
```

## Comparison with index

|                | `index`              | `attribute`          |
| -------------- | -------------------- | -------------------- |
| Data structure | Inverted (word→docs) | Forward (doc→value)  |
| Storage        | Disk                 | RAM (default)        |
| Text search    | ✅                   | ❌                   |
| Exact match    | ❌                   | ✅                   |
| Sorting        | ❌                   | ✅                   |
| Filtering      | ❌                   | ✅                   |
| Grouping       | ❌                   | ✅                   |

## Combining with index

```
field book type string {
    indexing: index | attribute | summary
}
```

- Search "gene" → finds "Genesis" (via `index`)
- Sort results alphabetically (via `attribute`)
- Filter exact `book = "Genesis"` (via `attribute`)

**Trade-off:** uses more memory since data is stored twice.
