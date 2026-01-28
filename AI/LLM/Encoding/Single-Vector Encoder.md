---
aliases:
  - Bi-encoder
---
**Bi-encoder** — *encodes* **documents** and **queries** <u><i>independently</i></u>
								into separate [[Embedding Vector|Vectors]],
	then compares them by [[Similarity Score|Similarity]]

- "Bi" = two separate encoder passes
	- One encodes the query → single [[Embedding Vector|Vector]]
	- One encodes the document → single [[Embedding Vector|Vector]]
- Document [[Embedding Vector|Vectors]] are precomputed and indexed offline
	- At query time, only the query needs [[Encoder]]
	- Search becomes a fast ANN lookup

Contrast with **Cross-encoder**:
- Cross-encoder feeds query + document **together** into one model
	- Tokens can attend to each other — more accurate
	- But requires a forward pass **per document** — doesn't scale
- Bi-encoder sacrifices that cross-attention
			for independent encoding and retrieval speed

> Limitation: entire document is compressed into one [[Embedding Vector|Vector]],
	 thus fine-grained token-level details get diluted.
> [[Contextualized Late Interaction over BERT|ColBERT]] addresses this by late interaction.

