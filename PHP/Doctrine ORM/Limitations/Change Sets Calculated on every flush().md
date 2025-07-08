---
aliases:
  - flush change sets
---
In [[Doctrine ORM]] when you call `flush()`, only then does it start to calculate change sets. Few flushes - few change sets, a lot of flushes - a lot.

