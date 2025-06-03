Use Activity Options `ActivityCancellationType::WaitCancellationCompleted`:

```php
ActivityOptions::new()
   ->withCancellationType($waitForCompleted)
```

This will ensure that activity is cancelled before throwing `CanceledFailure` during [[Workflow Cancellation]].