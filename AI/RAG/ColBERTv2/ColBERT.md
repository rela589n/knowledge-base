---
aliases:
  - ColBERT
  - Contextualized Late Interaction over BERT
docs:
  - https://www.youtube.com/watch?v=xTzUn3G9YA0
---
**ColBERT** - similar approach to [[Single-Vector Encoder|Bi-encoder]],
A hybrid approach: 
- [[ColBERT Encoding|Encodes]] query and document separately (like ),
  preserving granularity.
- Computes fine-grained matching at retrieval time

Larger storage, but much better results:
- Granularity:
	- Multi-topic queries don't get averaged away
	- Each query term finds best match independently
- Index-efficient
	- Document embeddings are precomputed and indexed  
	- "Late interaction" = only the final scoring step happens at query time

1. Documents are [[ColBERTv2 Index|Indexed]] ahead of time:
	- [[Token|Tokenized]] with [[Bidirectional Encoder Representations from Transformers|BERT]] tokenizer;
	- [[Encoder|Encoded]] with [[ColBERT Encoding|Clever Encoding]];
	- Each [[Embedding Vector|Vector]] is stored in the [[ColBERTv2 Index|Index]].
	
2. Queries are [[Token|Tokenized]] and [[Encoder|Encoded]] the same way;

3. [[ColBERTv2 Index|Index]] is looked up for candidates;

4. For every [[MaxSim]] score is computed:
   every query [[Token]] is scored against of document
	   and the highest is added to the overall score

Database: [[Vespa]]
Python lib (separate): [RAGatouille](https://github.com/AnswerDotAI/RAGatouille)
