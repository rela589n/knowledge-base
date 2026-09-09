---
aliases:
  - Symfony Lazy service argument reference
---
```php
// It must be lazy lest it creates circular reference:
$services
	->set(
		PropertyExceptionMappingPlanCompiler::class.'::$planRegistry',
		ObjectExceptionMappingPlanRegistry::class
	)->lazy()
	->factory('current')
	->args([[service(ObjectExceptionMappingPlanRegistry::class)]]);
```
