---
aliases:
  - Workers
---
[[Temporal]] workers are used to execute [[Temporal/Workflow|Workflows]].

Workers require [[RoadRunner]] to run. They use it's [[gRPC]] feature to poll [[Server|Temporal Service]] for the incoming [[Task|Tasks]].
