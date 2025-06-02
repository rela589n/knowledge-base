**Schedule-To-Close** [[Activity Timeouts|Activity Timeout]] is the complete time for [[Activity]] execution, including [[Retry Policy|retries]]. 

This timeout **prevents [[Activity]] from executing indefinitely**, and retrying indefinitely. This timeout is much better than [[Retry Policy]], since it's rare that retries could fix the situation.

> When setting [[Schedule-To-Close]] timeout, make sure that you set [[Schedule-To-Start]] timeout as well. Otherwise, it could be that activity starts almost at the end of timeout, and http request might not complete in time.

Be careful not to set a shorter value than [[Activity]] might need, since it may remain [[Activity Task Queue|queued up]] for some time (while timer is already ticking) before actually being taken by the [[Worker]]. To limit this, use [[Schedule-To-Start]] timeout.

Also, be aware that [[Retry Policy|retries]] could terminate prematurely if the timeout has already elapsed.

![[Activity Timeouts.png]]
