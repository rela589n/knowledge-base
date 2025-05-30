**Schedule-To-Close** [[Activity Timeouts|Activity Timeout]] is the complete time for [[Activity]] execution, including [[Retry Policy|retries]]. 

Beware of the situation when [[Activity Task]] may be Scheduled for some time before actually being taken as timer is already ticking.

Also, beware lest [[Retry Policy|retries]] terminate prematurely if not properly configured.

