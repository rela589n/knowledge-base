---
aliases:
  - compensations
---
[[SAGA pattern]]

[[Temporal/Temporal Server]] internally manages state of the [[Temporal/Workflow/Workflow|Workflows]].
It can be that [[Temporal/Workflow/Workflow|Workflow]] started [[Workflow Execution|Execution]] on one [[Worker]] (that eventually crased), continued on another [[Worker]], and finished on the third one.

Each activity class is wrapped to provide retry logic in case if requested service is temporarily down.

Temporal server internally manages queues so that activities could be executed in a scalable manner.
