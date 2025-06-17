---
aliases:
  - Side-Effect-Free
  - Pure Functions
---
[[Side-Effect]]-Free Functions safely express complex logic in the [[Code]]. These are the [[Query|Queries]] that doesn't produce any not anticipated consequences, and does not depend on any implicit sources, and thereby **they always produce the same result**, and are easily unit-tested.

Use [[CQS|Command-Query Separation]], make sure to [[Refactoring|Refactor]] mingled things into separate [[Command|Commands]] and [[Query|Queries]].

[[Value Object|Value Objects]] expose [[Side-Effect-Free Functions]]. They are easy to test, easy to use, easy to be combined. Consider leveraging them when writing [[Query|Queries]].
