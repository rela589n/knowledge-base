Temporal doesn't recommend to setting the timeouts for [[Temporal/Workflow/Workflow|Workflows]].

**Execution Timeout** - a complete timeout (including retries) for a [[Temporal/Workflow/Workflow|Workflow]] to execute.

**Run Timeout** - mostly used for [[Cron Job|Cron Jobs]].

**Task Timeout** - timeout for one particular [[Workflow Task]] to execute before it's sent to another [[Worker]]. Default is 10 seconds.
