---
aliases: []
---
**Attribute** field — stores field value **in RAM** as a forward index (document → value).

Like a database index — you query using the index,
  but you keep the underlying table ([[Document Store]]) to rebuild it when needed.

## Structure

Column-oriented — each field is a separate array indexed by document ID:

|        | popularity | chapter_num | book      |
| ------ | ---------- | ----------- | --------- |
| doc[0] | 42         | 1           | Genesis   |
| doc[1] | 99         | 1           | Exodus    |
| doc[2] | 17         | 1           | Leviticus |
| doc[3] | 83         | 1           | Numbers   |

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
An inverted index (value → docs) isn't suitable.

## Comparison with index

|                | `index`              | `attribute`         |
| -------------- | -------------------- | ------------------- |
| Data structure | Inverted (word→docs) | Forward (doc→value) |
| Storage        | Disk                 | RAM (default)       |
| Text search    | ✅                    | ❌                   |
| Exact match    | ❌ (depends)          | ✅                   |
| Sorting        | ❌                    | ✅                   |
| Filtering      | ❌                    | ✅                   |
| Grouping       | ❌                    | ✅                   |

### Combining with index

```vespa
field book type string {
    indexing: index | attribute | summary
}
```

- Search "gene" → finds "Genesis" (via `index`)
- Sort results alphabetically (via `attribute`)
- Search for `book = "Genesis"` (via `attribute`)

**Trade-off:** combined uses much more memory since data is stored twice.

## Memory implications

10 million documents × 100-byte attribute ≈ 1 GB RAM

### `paged` — letting OS manage memory

All attributes are persisted to disk as snapshots — both normal and paged.
The difference is what happens after startup:

```
Normal:  disk → load all into RAM → serve from RAM (disk sits idle)
Paged:   disk → memory-map       → OS caches what it can → page faults for the rest
```

```vespa
field book type string {
    indexing: attribute
    attribute: paged
}
```

Trade-offs:
- Latency becomes unpredictable (page faults when data is on disk)
- Throughput drops under memory pressure

Avoid `paged` with:
- [[HNSW index|HNSW]] indexing (random access pattern causes constant page faults)
- First-phase ranking (runs on every matched document)

## Configuration options

- **`fast-search`** — adds B-tree/hash index for faster lookups, more memory even for empty fields
- **`fast-access`** — keeps replicas in memory on all nodes for higher feed throughput

See also [[Vespa Attributes vs Elasticsearch Doc Values]]