---
aliases:
  - Workers
---
**[[Temporal]] Workers** execute [[Temporal/Workflow/Workflow|Workflows]].

Workers are **run on [[RoadRunner]]**.

PHP [[Worker Process]] <- [[RR Temporal Plugin]] <- [[Temporal Server|Temporal Service]]:

**[[RR Temporal Plugin]]** **polls [[Temporal/Temporal Server|Temporal Service]]** **for the incoming [[Task|Tasks]]**, and then **passes** them via [[Goridge]] **to PHP** [[Worker Process|Worker Processes]], which listen for the incoming [[Task|Tasks]].
