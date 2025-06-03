**Sticky Execution** - an optimization technique, that anticipates [[Temporal Server|Temporal Service]] sending [[Workflow Task|Workflow Tasks]] related to some [[Workflow Execution]] to the same [[Worker]] that accepted them earlier. 

Thus, it's likely that the [[Worker]] still keeps cached [[Workflow Execution]], and it won't need to do the [[Workflow Replay|Replay]].

Under the hood [[Temporal Server|Temporal Service]] creates [[Sticky Queue]], available only for this particular [[Worker]].
