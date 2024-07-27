---
aliases:
  - 2pc
  - distributed commit
repo: https://github.com/rela589n/two-phase-commit/tree/main
---
Uses transaction manager (coordinator) to control the overall transaction flow.

![[Pasted image 20240616181302.png]]
When participants reply "yes" to "prepare" request, this means no way can they refuse to commit the transaction later. All the votes are collected, and if all replied "yes", - then message is sent for everybody to "commit" (second phase).