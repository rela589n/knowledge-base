---
aliases:
  - Failure detection
  - retries
  - Retry Options
---
See [How Temporal Handles Failures](https://docs.temporal.io/encyclopedia/event-history/event-history-dotnet#How-History-Replay-Provides-Durable-Execution)

**Retry Policy** - [[Declarative]] specification of how [[Temporal/Workflow/Workflow|Workflow]] or [[Activity]] must be retried if fails.

[[Activity Retry Options]]
[[Workflow Retry Options]]

You define [[Retry Policy]] based on [[Types of Failures]].

> When charge is made based on api requests, it's better not to do much retrying.

Do not set max attempts to 1 just because your [[Activities Idempotence|Activity isn't idempotent]]. Network crash before http request will cause complete [[Workflow Execution Failure]].
