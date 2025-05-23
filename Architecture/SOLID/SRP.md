---
aliases:
  - Single Responsibility Principle
---
Every class must have only one "reason to change". 
Obedience leads to [[Protected Variations]] (changes are isolated).

This implies that any part of the system could only change due to one particular actor of the system asking for something.

For example, a violation of that principle could be when one endpoint is used by two features - reports and financial transactions list. If admin / user asks for the feature, this would lead to change in the same code, meaning it has at least 2 responsibilities.
