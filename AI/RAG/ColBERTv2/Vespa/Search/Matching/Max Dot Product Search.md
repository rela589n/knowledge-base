---
aliases:
  - Vespa Dot Product Search and Sort
  - Vespa Nearest Neighbour
---
See [tutorial](https://docs.vespa.ai/en/querying/nearest-neighbor-search-guide#maximum-inner-product-search-using-vespa-wand)

```shell
vespa query \
    'yql=select * from track where {targetHits:10}wand(tags, @userProfile)' \
    'userProfile={"gospel":10, "love songs":5}' \
    'hits=2' \
    'ranking=tags'
```

It searches those which have **max [[Inner Product|Dot Product]]**
between `doc.tags` and `query.userProfile`.

Then, [[rawScore()]] yields [[WAND]] score:

```sd
rank-profile tags {
    first-phase {
        expression: rawScore(tags)
    }
}
```

Tags is a [[Weighted Set]]:

```sd
field tags type weightedset<string> {
	indexing: summary | attribute
	attribute: fast-search
}
```

