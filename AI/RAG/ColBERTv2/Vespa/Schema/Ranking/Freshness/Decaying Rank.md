---
aliases:
  - Freshness Rank
docs:
  - https://docs.vespa.ai/en/ranking/nativerank.html#designing-our-own-blog-freshness-ranking-function
---
```
function freshness() {
    expression: exp(-1 * age(timestamp)/(3600*12))
}
```

![[Freshness Rank.png]]