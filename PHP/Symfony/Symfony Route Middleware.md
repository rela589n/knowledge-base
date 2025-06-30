Use this configuration:

```php
#[AsEventListener(KernelEvents::CONTROLLER_ARGUMENTS, priority: -1000)]
final class YourMiddleware
{
	public function __invoke(ControllerArgumentsEvent $event): void
	{
		$controller = $event->getController();

		$event->setController(
			static function (...$args) use ($controller) {
            // your middleware

            return $controller(...$args);
        });
	}
}
```