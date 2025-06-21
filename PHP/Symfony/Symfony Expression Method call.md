---
aliases:
  - Symfony migrations custom template expression path
---

```php
final readonly class DoctrineMigrationsTemplateCompilerPass implements CompilerPassInterface
{
    public function process(ContainerBuilder $container): void
    {
        $configurationDefinition = $container->getDefinition('doctrine.migrations.configuration');

        $methodCall = $this->getCustomTemplateMethodCall($configurationDefinition);

        if (null === $methodCall) {
            return;
        }

        [$customTemplate] = $methodCall[1];

        if (!str_starts_with($customTemplate, '@=')) {
            return;
        }

        $configurationDefinition->removeMethodCall('setCustomTemplate');
        $configurationDefinition->addMethodCall('setCustomTemplate', [new Expression(substr($customTemplate, 2))]);
    }

    /** @return ?array{string,array} */
    private function getCustomTemplateMethodCall(Definition $configurationDefinition): ?array
    {
        foreach ($configurationDefinition->getMethodCalls() as $call) {
            $methodName = $call[0];

            if ('setCustomTemplate' === $methodName) {
                return $call;
            }
        }

        return null;
    }
}
```
