---
aliases: []
---
**Attribute** field — stores field value **in RAM** as a forward index (document → value).

## Structure

Column-oriented — each field is a separate array indexed by document ID:

```
popularity:  [42, 99, 17, 83]
chapter_num: [1,  1,  1,  1 ]
book:        [Genesis, Exodus, Leviticus, Numbers]
```

- Lookup: `popularity[2]` → `17` (O(1))
- Sorting by `popularity` reads only the `popularity` array
  — never touches other fields → cache-friendly

## Enables

- Sorting (`order by book`)
- Filtering (`book = "Genesis"` exact match)
- Grouping (`group by book`)
- Range queries (`chapter_num > 5`)
- Fast access in ranking expressions

These operations require direct access to each document's value,
  which only a forward index (doc → value) can provide.
An inverted index (value → docs) maps the wrong way.

## Configuration options

- **`fast-search`** — adds B-tree/hash index for faster lookups, more memory even for empty fields
- **`fast-access`** — keeps replicas in memory on all nodes for higher feed throughput

## Memory implications

10 million documents × 100-byte attribute ≈ 1 GB RAM

### `paged` — spilling to disk

```vespa
field book type string {
    indexing: attribute
    attribute: paged
}
```

Memory-maps the file — the OS decides what stays in RAM and what spills to disk.

Trade-offs:
- Latency becomes unpredictable (page faults when data is on disk)
- Throughput drops under memory pressure

Avoid `paged` with:
- HNSW indexing (random access pattern causes constant page faults)
- First-phase ranking (runs on every matched document)

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

```vespa
field book type string {
    indexing: index | attribute | summary
}
```

- Search "gene" → finds "Genesis" (via `index`)
- Sort results alphabetically (via `attribute`)
- Filter exact `book = "Genesis"` (via `attribute`)

**Trade-off:** uses more memory since data is stored twice.
