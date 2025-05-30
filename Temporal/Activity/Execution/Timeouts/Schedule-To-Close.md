**Schedule-To-Close** [[Activity Timeouts|Activity Timeout]] is the complete time for [[Activity]] execution, including [[Retry Policy|retries]]. 

This timeout **prevents [[Activity]] from executing indefinitely**. This timeout is much better than [[Retry Policy]], since it's rare that retries could fix the situation.

Be careful not to set shorter value than [[Activity]] might need, since it may be [[Activity Task Queue|queued up]] for some time before actually being taken into work, and timer is already ticking. To limit this, use [[Schedule-To-Start]] timeout.

Also, be aware that [[Retry Policy|retries]] could be terminated prematurely if the timeout has already elapsed.

![[Activity Timeouts.png]]
