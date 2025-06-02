By default, [[Temporal/Workflow/Workflow|Workflows]] do not specify [[Retry Policy]], since [[Workflow Replay|Workflows are Deterministic]], and retrying them won't cause any change.

Yet it's possible, to retry the [[Workflow Execution]] itself by specifying [[Retry Policy]].
