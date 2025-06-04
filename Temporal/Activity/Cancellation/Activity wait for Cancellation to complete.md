Use Activity Options `ActivityCancellationType::WaitCancellationCompleted`:

```php
ActivityOptions::new()
   ->withCancellationType($waitForCompleted)
```

This will ensure that activity is cancelled before throwing `CanceledFailure` during [[Workflow Cancellation]]. Also, note that it works only within [[Activity Execution Timeouts|Execution Timeouts]].