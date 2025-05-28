You can [[Interrupting the Workflow|interrupt the Workflow]] right from the [[Temporal UI]], or programmatically.

It's possible that we'd want to have the ability to cancel a complex workflow (like notification campaign that requires a lot of manipulations: `Schedule`, `Run`, `SubscribeToTopic`, `Send`, `Complete`). If there was a business requirement to cancel notification campaign (even if it's running), it'd be possible with temporal.

