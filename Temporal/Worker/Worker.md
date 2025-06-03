---
aliases:
  - Workers
---
[[Temporal]] workers are used to execute [[Temporal/Workflow/Workflow|Workflows]].

Workers are run on [[RoadRunner]]. They use [[RR Temporal Plugin]] to poll [[Temporal Server|Temporal Service]] for the incoming [[Task|Tasks]], and then pass them by [[Goridge]] to PHP [[Worker Process|Worker Processes]] that listen for the incoming [[Task|Tasks]].
