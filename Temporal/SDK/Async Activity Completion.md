Inside of the [[Activity]] you can use following statement:

```
Activity::doNotCompleteOnReturn();
```

Then, complete it from completely another process:
```php
$client = $this->workflowClient->newActivityCompletionClient();

// Complete the Activity.
$client->completeByToken(
    base64_decode($taskToken),
    $result,
);
```

See [sample](https://github.com/temporalio/samples-php/tree/master/app/src/AsyncActivityCompletion)
