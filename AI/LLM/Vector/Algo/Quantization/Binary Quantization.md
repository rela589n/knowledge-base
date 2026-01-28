---
aliases:
  - pack_bits
---
**Binary Quantization** — compresses [[Embedding Vector|Vectors]]
	by converting each [[Dimension]] to a single bit (0 or 1).

- Values above a threshold (usually 0) become `1`,
  the rest become `0`;
- A 768-dim float32 [[Embedding Vector|Vector]] (3072 bytes) shrinks to 96 bytes
  (**32x** compression).

Similarity is computed via [[Hamming Distance]]
	instead of [[Inner Product|Dot Product]] — extremely fast on modern CPUs.

> Trade-off: lossy — magnitude information per [[Dimension]] is discarded.

- Works better with higher-dimensional embeddings
	- More bits = less relative information loss
