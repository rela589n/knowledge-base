---
aliases:
  - Posting Rules
---
**Posting Rules** provide way to untangle dependencies between entities that are used as a basis for the derived and the derived entities.

![[Posting Rule.png]]

Implementation options:
1. Eager Firing - On each Entry inserted into Account, all [[Posting Rule|Posting Rules]] are triggered;
2. 