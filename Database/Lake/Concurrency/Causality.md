---
aliases:
  - Causally Dependent
  - Happens-before
  - Dependent
---
**B** is ***causally dependent*** *on* **A** when it:
- ***knows*** *about* **A** 
- ***depends*** *on* **A**;
- ***builds*** *upon* **A**. 

On the other hand, **A** ***happens before*** **B**.

> **Example:**
> Question msg [[Causality|Happens-before]] response msg.

If **operations *are dependent*** on each other (no [[Concurrent operations|Concurrency]]), 
then **latter overwrite** former.

[[Capturing Causal Dependencies]]