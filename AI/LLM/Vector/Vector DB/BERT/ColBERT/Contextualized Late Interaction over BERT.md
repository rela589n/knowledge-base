---
aliases:
  - ColBERT
docs:
  - https://www.youtube.com/watch?v=xTzUn3G9YA0
---
**Col-[[Bidirectional Encoder Representations from Transformers|BERT]]** - creates contextual individual [[Embedding Vector|Vectors]] and compares them.
Much larger storage, but much better results.

- Preserves granularity
   - Multi-topic queries don't get averaged away  
   - Each query term finds its best match independently  
- Still efficient  
   - Document embeddings can be precomputed and indexed  
   - "Late interaction" = only the final scoring step happens at query time

1. *Tokenize*:
   ![[1 - Tokenize Documents.png]]
2. Contextually *Vectorize* Tokens:
   ![[2 - Vectorize Tokens.png]]
3. Compute [[Similarity Score]] ([[O (N**2)]]) for each token in your document and then overall score for the document:
   ![[3 - Compute Score.png]]

Database: [[Vespa]]
Python lib (separate): [RAGatouille](https://github.com/AnswerDotAI/RAGatouille)
