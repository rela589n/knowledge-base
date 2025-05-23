When [[Workflow Execution]] reaches the limit of [[Event History]], it may continue as new with a fresh [[Event History]].

```php
// The current workflow run stops executing after this call.

return Workflow::newContinueAsNewStub(self::class)
    ->execute($params);
```