---
aliases:
  - Single Responsibility Principle
---
Every class must have only one "reason to change".

This implies that any part of the system could only change due to one particular actor of the system asking for something.

For example, a violation of that principle could be when one endpoint is used by both features of reports and financial transactions. If any asks for the feature, this would mean change to the same code, meaning the principle is violated.
