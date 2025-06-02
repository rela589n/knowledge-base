---
aliases:
  - Terminate a Workflow
  - Kill a Workflow
---
[[Temporal/Workflow/Workflow|Workflow]] Termination is a forceful stop of a [[Workflow Execution]]
All running  [[Activity Cancellation|Activities are "Canceled"]] (fail on [[Activity Heartbeat|Heartbeat]]).
No [[SAGA|compensations]] are executed, and Thus [[Workflow Cancellation]] is preferred way.

