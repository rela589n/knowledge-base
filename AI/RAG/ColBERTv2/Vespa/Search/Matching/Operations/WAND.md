---
aliases: ["WAND", "Weak AND"]
---
**WAND** operator returns the same top-k [[Inner Product|Dot Product]]-sorted results as the brute-force [[dotProduct()]] query operator.

It performs [[Matching]] and [[Ranking]] interleaved and skips the documents which are not relevant for the final top-k results.
