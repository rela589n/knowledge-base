**Sticky Execution** - an optimization technique, that implies that includes [[Server|Temporal Service]] sending [[Workflow Task|Workflow Tasks]] about some [[Workflow Execution]] to the same [[Worker]] that accepted them earlier.

Under the hood [[Server|Temporal Service]] creates [[Sticky Queue]], available only for this particular [[Worker]].