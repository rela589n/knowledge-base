---
aliases:
---
**Document Store** — compressed serialized blobs of full documents on disk.

Source of truth — stores **all fields** regardless of `indexing` config.

Used for:
- Document GET (`/document/v1/...`)
- Re-indexing on schema change (no need to re-feed from external source)
- Serving non-attribute [[Document Summary|summary]] fields

## Physical structure

- `.dat`/`.idx` file pairs
- Append-only — only the last pair is writable, older pairs are immutable
- Data written in **chunks** (~16KB), compressed (e.g. zstd)
- In-memory LID → position mapping for lookups

## Compaction

Updates create new versions in new files, old versions remain.
Periodic compaction rewrites active documents, drops obsolete versions.

Not like [[SSTable]] merge — no sorting involved, just garbage collection.

Essentially an **append-only heap** (similar to PostgreSQL's table heap):
- Unordered storage, addressed by LID (like `ctid` in PostgreSQL)
- Bloat from updates, cleaned up by compaction (like `VACUUM`)
- Unlike a heap, strictly append-only — no in-place updates

## Query-time behavior

Accessed **only** when non-attribute summary fields are needed.

Retrieving even one field requires:
1. Read and decompress the whole **chunk**
2. Deserialize the full **document blob**
3. Extract the needed field

Row-oriented — wasteful for single field access.

The default summary includes `documentid` which lives here
  → always hits disk unless using a custom attribute-only summary.

## Prefer paged attributes over document store

For fields that appear in query responses regularly,
  a [[Indexing Attribute field|paged attribute]] is better than document store fallback:

- Paged attribute reads only the **one field** needed (column-oriented)
- Document store reads the **entire blob** for one field

Fall back to document store only when a field is:
- Rarely accessed in queries (e.g. only via direct GET)
- Too large to justify even memory-mapped overhead
