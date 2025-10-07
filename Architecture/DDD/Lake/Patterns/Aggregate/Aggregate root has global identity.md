---
aliases:
  - Association Traversal
---
Only [[Aggregate Root]] can be obtained by the database query.

It makes sense to create [[Repository]] only for [[Aggregate Root]] objects, and use [[Association Traversal]] for the rest.
