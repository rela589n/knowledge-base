[[Workflow Task Queue]], exclusive for one particular [[Worker]] for the purposes of [[Sticky Workflow Execution]]. 

If [[Worker]] fails to read the item from that queue shortly after scheduled, it's redirected to the original [[Workflow Task Queue]], so that any [[Worker]] would be able to pick it up.
