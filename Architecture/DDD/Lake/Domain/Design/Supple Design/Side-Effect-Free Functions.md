---
aliases:
  - Side-Effect-Free
  - Pure Functions
---
**[[Side-Effect]]-Free Functions** are [[Query|Queries]] that **don't produce** any **unanticipated [[Side-Effect|Consequences]]**, and do not depend on any implicit sources, and thereby **always produce** the **same result**, and are **easily unit-tested**. They safely express complex logic in the [[Code]].

> Use [[CQS|Command-Query Separation]], and make sure to [[Refactoring|Refactor]] mingled things into separate [[Command|Commands]] and [[Query|Queries]].

**Complex logic and calculations** should be exposed as [[Value Object]] methods that implement [[Side-Effect-Free Functions]]. 

They are easy to test, easy to use, and easy combine. Consider leveraging them to answer [[Query|Queries]].
