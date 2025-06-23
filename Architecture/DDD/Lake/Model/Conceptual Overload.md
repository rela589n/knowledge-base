---
aliases:
  - Standalone Class
---
Every [[Association]], every dependency contributes to conceptual load. To **understand the class** we must understanding the **relationship with its dependencies**.

The more things we have to keep in mind to understand the concept, the more overloaded it becomes.

[[Expressing Concepts Explicitly|Implicit Concepts]] contribute to load even more than explicit dependencies. They also need to be understood, but they are "ghosts" whose existence we can only imply.

**[[Low Coupling & High Cohesion|Low Coupling]]** is fundamental to **cope with conceptual load**. Each [[Module]], each class must be as self-contained as possible (Standalone Classes).

There must be **least references** to other [[Module|Modules]] and classes, so that they **can be understood by themselves** w/o any references.
