---
aliases:
  - Terminate the Workflow
  - Kill the Workflow
---
[[Workflow Execution|Workflow]] Termination is a forceful stop of a [[Workflow Execution]]
All running  [[Activity Cancellation|Activities are marked for Cancellation]] (will fail on [[Activity Heartbeat|Heartbeat]]).
No [[SAGA|compensations]] are executed, and therefore it's last resort!  In almost every scenario [[Workflow Cancellation]] should be used instead. Use only when [[Workflow Execution|Workflow]] is in unrecoverable state.

[[Temporal CLI Terminate Workflow]]

