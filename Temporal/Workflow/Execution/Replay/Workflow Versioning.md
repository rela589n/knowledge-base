---
aliases:
  - Workflow Patching
---
Refs: [sdk documentation](https://docs.temporal.io/develop/php/versioning#php-sdk-patching-api)

We can't just make changes to [[Temporal/Workflow/Workflow Definition|Workflow Definition]] and think that everything will work just fine. Such changes can result in [[Workflow Replay]] consistency.

> It's [[Temporal/Workflow/Workflow Definition|Workflow Definition]] **Changes that are versioned**, not the [[Temporal/Workflow/Workflow Definition|Workflow Definition]] itself.

How versioning works when added:

1. If the existing workflow has already passed to the next step, this change will be ignored.
2. If it hasn't passed to the step, it will be applied as most recent.

During the [[Workflow Replay|replay]] temporal uses `-1`  as a starting version for already executed code. IOW, if `Workflow::getVersion()` is added to the place which code has already executed, then "-1" is returned.

If the workflow hasn't yet executed further commands, and thus a newly added version call, the maximum supported version is used.

> `Workflow::getVersion()` returns the same version for multiple calls if given id is the same. Keep that in mind, when using it in the loops.

### Querying for versions

To **query** for already running workflow versions, you must enable ElasticSearch.
![[Query Workflow versions.png]]

### Testing

To **test** that old version of the workflow will continue to work, you may get [[Event History]] json, and use [[WorkflowReplayer]] to run it in the tests.
