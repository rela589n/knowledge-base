```php
#[Autowire('@=env("bool:APP_CONSUMERS_SYNC_MODE") ? 1 : 256')]
private int $chunkSize,
```


