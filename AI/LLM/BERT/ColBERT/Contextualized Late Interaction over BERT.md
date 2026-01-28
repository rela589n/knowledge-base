---
aliases:
  - ColBERT
docs:
  - https://www.youtube.com/watch?v=xTzUn3G9YA0
---
**Col-[[Bidirectional Encoder Representations from Transformers|BERT]]** - keeps contextual [[Embedding Vector|Vectors]] for each token.
Larger storage, but much better results.

- Preserves granularity
   - Multi-topic queries don't get averaged away
   - Each query term finds best match independently
- Index-efficient
   - Document embeddings are precomputed and indexed  
   - "Late interaction" = only the final scoring step happens at query time

1. *Tokenize*:
   ![[1 - Tokenize Documents.png]]
2. Contextually *Vectorize* Tokens:
   ![[2 - Vectorize Tokens.png]]
3. Compute [[MaxSim]] score ([[O (N**2)]]): score each token in your document and then combine into an overall score:
   ![[3 - Compute Score.png]]

Database: [[Vespa]]
Python lib (separate): [RAGatouille](https://github.com/AnswerDotAI/RAGatouille)
