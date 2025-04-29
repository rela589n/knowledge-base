You can use `IGNORED_ATTRIBUTES` to skip trace from being included in the logs.

```php
try {
    $uuid = Uuid::fromString('2f0e00553-577e-7f99-9eca-b4b2530758e3');

    throw new UserNotFoundException($uuid);
} catch (Exception $e) {
    $context = $service->serializer->normalize($e, 'json', [
        AbstractNormalizer::IGNORED_ATTRIBUTES => ['trace', 'traceAsString'],
    ]);

    dd($context);
}
```

Example output:

```json
{
    "message": "Invalid UUID: \"2f0e00553-577e-7f99-9eca-b4b2530758e3\".",
    "file": "\/app\/vendor\/symfony\/uid\/Uuid.php",
    "value": "2f0e00553-577e-7f99-9eca-b4b2530758e3",
    "type": "0",
    "line": 42,
    "code": 0,
    "previous": null
}
```