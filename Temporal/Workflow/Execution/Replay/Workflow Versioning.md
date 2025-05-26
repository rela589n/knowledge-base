---
aliases:
  - Workflow Patching
---
Refs: [sdk documentation](https://docs.temporal.io/develop/php/versioning#php-sdk-patching-api)

We can't just make changes to [[Temporal/Workflow/Workflow Definition|Workflow Definition]] and hope that everything will work just fine. The problem is with [[Workflow Replay]] consistency.

We don't version the whole [[Temporal/Workflow/Workflow Definition|Workflow Definition]], instead we **version the changes**.

How versioning works:

1. If the existing workflow has already passed to the next step, this change will be ignored.
2. If it hasn't passed to the step, it will be applied.

Temporal uses `-1` as a starting version for already running workflows.

If the workflow hasn't yet executed the next command, a max supported version will be used

If Workflow::getVersion() is added after the code has already executed the next activity, then "-1" is used, and the default (previous) version is executed.

Changes to the timers (except 0-related changes) do not have to be versioned (already scheduled timer will be the one).
### Querying for versions

To **query** for already running workflow versions, you must enable ElasticSearch.
![[Query Workflow versions.png]]

### Testing

To **test** that old version of the workflow will continue to work, you may get [[Event History]] json, and use [[WorkflowReplayer]] to run it in the tests.
