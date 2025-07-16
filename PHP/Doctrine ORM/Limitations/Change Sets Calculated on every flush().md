---
aliases:
  - flush change sets
---
In [[Doctrine ORM]] when you call `flush()`, only then does it start to calculate change sets. Few flushes - few change sets, quite a few flushes - a lot of change sets.

See [Deferred Implicit Change Tracking Policy](https://www.doctrine-project.org/projects/doctrine-orm/en/3.5/reference/change-tracking-policies.html#deferred-implicit)  

There's [Deferred Explicit Change Tracking Policy](https://www.doctrine-project.org/projects/doctrine-orm/en/3.5/reference/change-tracking-policies.html#deferred-explicit) that only keeps track of entities that have been explicitly marked for change tracking by `$em->persist()` operation.
