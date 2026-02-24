---
aliases:
  - Vector
  - Token Vector
  - Embedding
  - Dense Representations
---
**Embedding Vector** is multi-[[Dimension|Dimensional]] point that represents a <u><b>direction of thought</b></u>. A position in a meaning-space.

Characteristics:
- [[Dimension]]
- Data type
- [[Distance Metric|Distance Metric]]

![[3D Vectors Angles.png]]

Similar things are close to each other.

![[BlowBall.png]]
(see [[Vespa - Intro into Vector Search]])

![[Similar Words - Similar Vectors.png]]

If there are few thoughts in one sentence,
building one vector for it will bring worse results
		than having one thought per prompt:
- Multi-topic queries get "averaged" into one vector                          
    - Semantic meaning gets diluted
- Retrieved chunks may only match the "dominant" topic            
    - Other topics in the query get under-represented 

ColBERT tries to solve that.

![[Embedding Vector is one Direction.png]]