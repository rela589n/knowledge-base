**Who can create who.**

Class **A *creates* B** if:
- **A** is an **[[Aggregate Root]]**, while **B** is the **inner** entity 
  of the [[Aggregate]] (see [[Aggregate factory method]]);
- **A** has **composition** over **B**;
- **A** has the **information** needed to create **B**.

Related to [[Creational Design Patterns]]