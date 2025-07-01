---
aliases:
  - Standalone Class
---
Every [[Association]], every dependency contributes to conceptual load. To **[[Understanding|Understand]] the class** it's needed to [[Understanding|Understand]] the **relationship with its dependencies**.

The bigger is the **number of things we have to keep in mind** to understand the [[Domain Concept|Concept]], the more overloaded it becomes.

[[Expressing Concepts Explicitly|Implicit Concepts]] contribute to load even more than explicit dependencies. They also needed to be understood, but it's harder as they are "ghosts" whose existence we can only imply.

**[[Low Coupling & High Cohesion|Low Coupling]]** (defining [[Conceptual Boundary|Conceptual Boundaries]]) is fundamental to **coping with [[Conceptual Overload|Conceptual Load]]**. Each [[Module]], each Class must be as self-contained as possible (Standalone Classes). 

There must be **least references** to other [[Module|Modules]] and classes, so that they **can be understood by themselves** w/o any references.
