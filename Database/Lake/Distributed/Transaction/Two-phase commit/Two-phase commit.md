---
aliases:
  - 2PC
  - Distributed Commit
repo: https://github.com/rela589n/two-phase-commit/tree/main
---
Uses transaction manager to control the overall transaction flow.

![[Two-phase commit.png]]
When participants reply "yes" to "prepare" request, this means no way can they refuse to commit the transaction later. All the votes are collected, and if all replied "yes", - then message is sent for everybody to "commit" (second phase).