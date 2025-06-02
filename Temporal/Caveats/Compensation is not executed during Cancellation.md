With this code, [[SAGA|compensation]] will not be executed during [[Workflow Cancellation]]:

```php
try {
    return yield $this->video->render($length);
} catch (Exception $e) {
    yield $this->video->cancel($length);

    throw $e;
}
```

This works in case of activity failure, but not in case of [[Workflow Cancellation]]. To solve it, use detached [[Workflow Async Operations]], or `Saga` object.
