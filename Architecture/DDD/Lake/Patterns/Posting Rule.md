---
aliases:
  - Posting Rules
---
**Posting Rules** provide way to **untangle dependencies** between **the entities** used as a basis for the derived **and the derived entities** themselves.

![[Posting Rule.png]]

> It could be that input and output of [[Posting Rule]] differs, yet the conception is the same.

Initiation models:
1. **Eager Firing** - On each Account ([[Aggregate Root]]) Entry inserted, it triggers all [[Posting Rule|Posting Rules]] right away;
2. **Aggregate-based Firing** - at some point Account triggers its [[Posting Rule|Posting Rules]] to process for new collected Entries;
3. **[[Posting Rule]]-based Firing** - initiated by external agent, which tells [[Posting Rule]] to fire. In this case, it's [[Posting Rule|Posting Rule's]] responsibility to identify Account Entries collected since the last run (for example via [[Overflow-reliable update sequence number comparison|Import Number]]). 
