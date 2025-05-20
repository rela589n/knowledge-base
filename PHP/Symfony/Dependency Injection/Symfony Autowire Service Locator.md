You can autowire container with services, tagged by particular tag:

```php
#[AutowireLocator('temporal.activity')]
ServiceProviderInterface $container,
```

