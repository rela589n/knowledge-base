**Schedule-To-Close** [[Activity Timeouts|Activity Timeout]] is the complete time for [[Activity]] execution, including [[Retry Policy|retries]]. 

This timeout **prevents [[Activity]] from executing indefinitely**. This timeout is much better than [[Retry Policy]], since it's rare that retries could fix the situation.

Beware of the situation when [[Activity Task]] may be Scheduled for some time before actually being taken into work (timer is already ticking).

Also, be aware that [[Retry Policy|retries]] could terminate prematurely if the timeout is already elapsed.

![[Activity Timeouts.png]]
