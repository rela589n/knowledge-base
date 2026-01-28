**Cross-encoder** — *accepts*  both **query** and **document**
	and *outputs* a **[[Similarity Score|Relevance Score]]** directly (not an [[Embedding Vector|Vector]]).

- Both texts concatenated: `[CLS] query [SEP] document [SEP]`
	- All tokens attend to each other across query and document
- Output is a scalar score (e.g. 0.0–1.0)
	- No vector produced — nothing to precompute or index
- Most accurate approach for relevance ranking
	- Full cross-attention captures fine-grained token interactions

**Doesn't scale**: requires a forward pass
	for every (query, document) pair.

Typical role — **re-ranker**:
- A [[Single-Vector Encoder]] retrieves top-k candidates cheaply
- Cross-encoder re-scores those candidates for precision
