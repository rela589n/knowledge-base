With this code, compensation will not be executed:

```php
try {
    return yield $this->video->render($length);
} catch (Exception $e) {
    yield $this->video->cancel($length);

    throw $e;
}
```

Well, actually it will work in case of activity failure, but not in case of [[Workflow Cancellation]].
