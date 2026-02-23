---
docs:
  - https://docs.vespa.ai/en/reference/nativerank.html
---
**nativeRank()** has similar characteristics as [[Best Match 25|BM25]] but also considers the proximity between matched terms in the document.

Unlike [[Best Match 25|BM25]], nativeRank has a normalized  score range: `[0,1]`, while [[Best Match 25|BM25]] has it unbound.

