It's possible to provide BC for:

```yaml
servers:
	option: value
```

that will be normalized into:

```yaml
servers:
	default: # <server_name>
		option: value
```

See `/nelmio/api-doc-bundle/src/DependencyInjection/Configuration.php:104`

```php
->beforeNormalization()
    ->ifTrue(function (array $v) {
        return 0 === count($v) || isset($v['option']);  
    })
    ->then(function (array $v): array {  
        return ['default' => $v];  
    })
->end()
```
