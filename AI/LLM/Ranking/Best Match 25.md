---
aliases:
  - BM25
---
**BM25** — a lexical **ranking function** that scores documents 
	by raw keywords (stems) w/o semantic understanding:
- **TF** (Term Frequency):
  how often the term appears in the document
	- Saturates — repeated terms have diminishing returns
- **IDF** (Inverse Document Frequency):
  how rare the term is across all documents
	- Rare terms are more important
- Document **length normalization**:
  penalizes long documents slightly

Limitation: no semantic understanding
- Misses synonyms, paraphrases

Why it's still used
- Extremely fast — simple math, no neural network
- No precomputation of embeddings needed
- Strong baseline that's hard to beat on some benchmarks
