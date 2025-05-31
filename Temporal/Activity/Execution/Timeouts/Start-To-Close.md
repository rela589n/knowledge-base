**Start-To-Close** [[Activity Timeouts|Activity Timeout]] - timeout for a single [[Activity Task]] execution.

If first [[Worker]] started [[Activity]] execution, and it didn't manage to complete within a timeout time, it's considered failed and a next attempt is launched ([[Retry Policy]]).


![[Start-To-Close Timeout.png#center|500]]

