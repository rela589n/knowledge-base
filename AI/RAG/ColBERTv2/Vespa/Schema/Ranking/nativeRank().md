---
docs:
  - https://docs.vespa.ai/en/reference/nativerank.html
---
**nativeRank()** has similar characteristics as [[Best Match 25|BM25]] but also considers the proximity between matched terms in the document.

Unlike [[Best Match 25|BM25]], which has an unbound score range,
Vespa’s nativeRank is normalized to a score in the range `[0,1]`.

