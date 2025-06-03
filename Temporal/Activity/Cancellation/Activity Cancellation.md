You can cancel the [[Activity]], if it [[Activity Heartbeat|heartbeats]].

Cancellation can originate from:
- [[Workflow Cancellation]] ([[Workflow Execution|Workflow's]] current [[Activity|Activities]] are cancelled);
- When [[Activity Timeouts|Activity Times-out]];
- Explicit Cancel of child task ([[Workflow Async Operations]]).

From [[Activity]]'s point of view, an exception (one of the descendants of `ActivityCompletionException`) is thrown when it tries to `Activity::heartbeat($i)`.

There's `cancellationType` option in [[Activity Options]]. Depending on it, [[Workflow Cancellation]] will behave differently.

