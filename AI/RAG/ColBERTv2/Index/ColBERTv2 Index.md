
## Index Structure

All document token [[Embedding Vector|Embeddings]] are stored in one [[ANN index]]
  Each [[Embedding Vector|Embedding]] is tagged with source document ID
  
```
Index entry: (vector, doc_id, token_position)
```

## Query Time Process

1. **[[Encoder|Encode]] Query** → token [[Embedding Vector|Embeddings]] `[q1, q2, q3, ...]`

2. **[[ANN index]] Search Per Token [[Embedding Vector|Vector]]** — each query token [[Embedding Vector|Vector]] finds K nearest neighbors:
```
q1 → [(doc_42, score), (doc_17, score), ...]
q2 → [(doc_17, score), (doc_42, score), ...]
q3 → [(doc_8, score), (doc_42, score), ...]
```

3. **Aggregate by Document** — collect all document IDs that appeared
   - Documents matching multiple query tokens → strong candidates
   - Take union or weight by frequency

4. **Full MaxSim on Candidates** — only ~1000 candidates
   - Load their token embeddings
   - Compute exact MaxSim score

## Why This Works

Good documents match **multiple** query tokens
  Naturally bubble up in aggregation

[[ANN index]] search: [[O (log N)]] per token, not [[O (N)]] traversal.
