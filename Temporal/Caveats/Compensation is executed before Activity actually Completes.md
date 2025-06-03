Activity sends http request that takes long time.
[[Activity Execution Timeouts|Activity Execution Timeout]] is elapsed.
Compensation is executed (no-op due to [[Idempotence]] check).
Http request succeeds.
Workflow is already closed, compensation executed, but state polluted.
