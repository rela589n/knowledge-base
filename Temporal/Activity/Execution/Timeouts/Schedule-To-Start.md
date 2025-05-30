**Schedule-To-Start** [[Activity Timeouts|Activity Timeout]] - how long for the [[Activity Task]] is allowed to be [[Activity Task Queue|queued up]] w/o being taken by any of the workers. Guarantees that [[Activity]] is started within a time-frame.

The timeout is crucial in scenarios like [[Worker]] failure. If no [[Worker]] is available to process, it would never start, it would pollute [[Task Queue]], and it'd be like "stuck situation".

Also it makes sense to set this timeout for the first task in the workflow to ensure that consumers aren't overloaded and to prevent the complete failure.

![[Schedule-To-Start Timeout.png]]
