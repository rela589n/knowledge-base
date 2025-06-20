---
aliases:
  - Side-Effect-Free
  - Pure Functions
---
[[Side-Effect]]-Free Functions safely express complex logic in the [[Code]]. These are the [[Query|Queries]] that don't produce any unanticipated consequences, and do not depend on any implicit sources, and thereby **always produce the same result**, and are **easily unit-tested**.

> Use [[CQS|Command-Query Separation]], and make sure to [[Refactoring|Refactor]] mingled things into separate [[Command|Commands]] and [[Query|Queries]].

Complex logic and calculations should be exposed as [[Value Object|Value Objects]] that implement [[Side-Effect-Free Functions]]. They are easy to test, easy to use, easy to be combined. Consider leveraging them to answer [[Query|Queries]].
