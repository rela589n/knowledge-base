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

> When every api request charged, it makes sense not to do much retrying.

Do not set max attempts to 1 just because your [[Activities Idempotence|Activity isn't idempotent]]. Network crash before http request will cause complete [[Workflow Execution Failure]].

You can specify non-retryable errors during the call time (`withNonRetryableExceptions`). Yet, beware that it doesn't include classes hierarchy, and works only on FQCN basis. 

Non-retryable errors are matched by previous exceptions as well. So, if you throw `ApplicationFailure(nonRetryable:false)` with previous `$e=ServerException`, and `ServerException` is part of `nonRetryableExceptions`, then it won't be retried anyway.


