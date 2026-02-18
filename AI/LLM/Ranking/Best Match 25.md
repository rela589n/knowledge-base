---
aliases:
  - BM25
---
**BM25** — a lexical **ranking function** that scores documents 
	*by*  **raw keywords** (stems) w/o semantic understanding:
- **TF** (Term Frequency):
  how often the term appears in the document
	- Saturates — repeated terms have diminishing returns
- **IDF** (Inverse Document Frequency):
  how rare the term is across all documents
	- Rare terms are more important
- Document **length normalization**:
  penalizes long documents slightly

> It's 3-4 times faster than nativeRank() [[Vespa]].

Limitation: no semantic understanding
- Misses synonyms, paraphrases

Why it's still used
- Extremely fast — simple math, no neural network
- No overhead of embeddings is needed
