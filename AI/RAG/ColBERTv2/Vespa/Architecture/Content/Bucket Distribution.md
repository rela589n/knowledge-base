**Bucket Distribution** — how Vespa maps documents to storage units called buckets.

## Document ID → Location

Every document ID hashes to a 58-bit numeric location:

```
"id:shop:product::iPhone15"  →  hash  →  0x02A4F3...B7E1
```

Only the **least significant bits (LSB)** matter for bucketing.

## Bucket Definition

A bucket = all documents sharing the same N least significant bits.

```
Document A:  ...1101 0101  →  bucket "0101"
Document B:  ...0010 0101  →  bucket "0101"  (same)
Document C:  ...1101 0110  →  bucket "0110"  (different)
```

## Bit Depth Controls Bucket Count

| Bits used | Max buckets | Docs per bucket (1M total) |
|-----------|-------------|----------------------------|
| 8 bits    | 256         | ~4,000                     |
| 12 bits   | 4,096       | ~250                       |
| 16 bits   | 65,536      | ~15                        |

More bits → more buckets → fewer documents each

## Splitting (Growth)

Bucket too large → add one more bit → splits into two.

**Before (8 bits):**
```
Bucket "0000 0101":  Doc A (...0 0000 0101)
                     Doc B (...1 0000 0101)
```

**After (9 bits):**
```
Bucket "0 0000 0101":  Doc A
Bucket "1 0000 0101":  Doc B
```

## Joining (Shrinkage)

Buckets too small → remove one bit → merge into one.

**Before (9 bits):**
```
Bucket "0 0000 0101":  Doc A
Bucket "1 0000 0101":  Doc B
```

**After (8 bits):**
```
Bucket "0000 0101":  Doc A, Doc B
```

## Key Properties

- **Automatic** — Vespa splits/joins without manual intervention
- **Local operation** — no data moves between nodes during split/join
- **Consistent** — document always hashes to same location

## See Also

- [[Content Cluster]]
- [[Content Cluster Scaling]]
