---
aliases:
  - Vespa Indexing Pipelines
---
Vespa's `indexing` directive defines ***how*  field** data *is* ***processed*** and ***stored***, determining how it will be queried.

## Operations

| Operation   | Purpose                                        |
| ----------- | ---------------------------------------------- |
| `summary`   | Makes field available in responses             |
| `index`     | Full-text on-disk index (if `string`)          |
| `attribute` | Store in memory (sorting, filtering, grouping) |

## Pipeline

The Pipe `|` chains operations — data flows through each in order:

```
indexing: input | lowercase | index | summary
```

- Order matters for **transformations** (e.g., `lowercase`)
- Order doesn't matter for **terminal operations** (`summary`, `index`, `attribute`)

## Combinations

**Only `summary`:**
- Returned in results
- Not searchable

**Only `index`:**
- Searchable
- Not returned in results

**Both `summary | index`:**
- Searchable and returned

## Example

```
schema scripture {
    document scripture {
        field book type string {
            indexing: index | summary      # search + return
        }
        field full_text type string {
            indexing: index                # search only
        }
        field chapter_num type int {
            indexing: summary | attribute  # return + filter
        }
    }
}
```
