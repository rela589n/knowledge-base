You can cancel the [[Activity]], if it [[Activity Heartbeat|heartbeats]].

When [[Workflow Cancellation]] happens, it's current [[Activity|Activities]] are cancelled.

When [[Activity Timeouts|Activity Times-out]], it is considered Cancelled.

From [[Activity]]'s point of view, exception (one of the descendants of `ActivityCompletionException`) is thrown when it tries to `Activity::heartbeat($i)`.
