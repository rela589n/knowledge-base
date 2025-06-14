When [[Workflow Execution]] has a prolongued [[Event History]], or if it has a long iteration duration (long sleep time, like subscription), it is better to continue it as new [[Workflow Execution]] with a fresh [[Event History]].

```php
// The current workflow run stops executing after this call.

return Workflow::newContinueAsNewStub(self::class)
    ->execute($params);
```

Or

```php
return Workflow::continueAsNew(
    Workflow::getInfo()->type->name,
    $params,
);
```