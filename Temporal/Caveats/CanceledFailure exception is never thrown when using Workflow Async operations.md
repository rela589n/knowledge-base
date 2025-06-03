Beware that [[Workflow Async Operations]] must *use `yield` for everything*, and not just return the given activity promise. 

For example:

```php
$p = Workflow::async(fn () => $this->activity->call($params));
```

Even though this code will work just fine in therms of "working", but it will cause great problems if such workflow will have to be [[Workflow Cancellation|Cancelled]]. Currently it never throws during cancellation 🫤.

Therefore, just keep this in mind, and ***always* use `yield`** 🙂:

```php
$p = Workflow::async(fn () => yield $this->activity->call($params));
```
