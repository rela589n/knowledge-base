---
aliases:
  - Reset the Workflow
---
**[[Workflow Execution|Workflow]] Resetting**  is terminating current problematic [[Workflow Run]], and starting new one with [[Event History]] being reset to the particular position (last successful event).

For example, if a long unintended [[Timer]] was started, you might deploy a quick fix and reset the workflows to the [[Workflow Event|Place]] before that [[Timer]] start.

Besides that, it's possible to keep [[Signal|signals]] and [[Update|updates]], so that the workflow will continue in a different direction.
