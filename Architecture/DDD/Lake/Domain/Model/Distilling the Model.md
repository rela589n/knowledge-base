---
aliases:
  - Model Distillation
---
[[Domain Model]] is the [[Model (generic)|Model]], - it should contain **bare minimum** of things that do actually **closely relate** to the [[Domain Concept|Domain Concepts]].

[[Strategic Distillation]]

We should ***drop*** all the **excessive things**, not important to the [[Code|Implementation]], *as* **those *contribute*** *to* **[[Conceptual Overload]]**.

Each **class** must be *[[Comprehension|Understood]]* with **minimum references** to other classes. 
Each **[[Association]]** must *embody* something **fundamental *to the* [[Comprehension|Meaning]]** of the object. 

Anything else must be [[Extracting a hidden concept|Extracted Elsewhere]]. 
You can ***draw on* [[Established Formalisms|Established Formalisms]]**, 
and ***revolve*** it ***around*** a **[[Value Object]]**.

**[[Low Coupling & High Cohesion|Low Coupling]]** is crucial. 
Each [[Module]], each class must be self-contained. 
They must be [[Comprehension|Understood]] with least references to other [[Module|Modules]] and classes.


