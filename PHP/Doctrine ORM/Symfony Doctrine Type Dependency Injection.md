
```php
// Doctrine Type

final class YourCustomType extends Type
{
    public const NAME = 'your_custom_type';

    private YourCustomService $yourCustomService;

    public function setYourCustomService(YourCustomService $yourCustomService): void
    {
        $this->yourCustomService = $yourCustomService;
    }

    public function convertToDatabaseValue($value, AbstractPlatform $platform): mixed
    {
        if (!is_string($value)) {
            return parent::convertToDatabaseValue($value, $platform);
        }

        return $this->yourCustomService->convertToDatabaseValue($value);
    }

    public function convertToPHPValue($value, AbstractPlatform $platform): mixed
    {
        if (!is_string($value)) {
            return parent::convertToPHPValue($value, $platform);
        }

        return $this->yourCustomService->convertToPHPValue($value);
    }

    public function getSQLDeclaration(array $column, AbstractPlatform $platform): string
    {
        return $platform->getStringTypeDeclarationSQL($column);
    }

    public function getName(): string
    {
        return self::NAME;
    }
}

// Type DI middleware

final readonly class YourCustomTypeBootstrapMiddleware implements Middleware
{
    public function __construct(
        #[Autowire('@your.custom.service')]
        private YourCustomService $service,
    ) {
    }

    public function wrap(Driver $driver): Driver
    {
        /** @var YourCustomType $type */
        $type = Type::getType(YourCustomType::NAME);

        $type->setYourCustomService($this->service);

        return $driver;
    }
}
```

Also there's a compiler pass to register custom middleware for connection (yet it <u>doesn't seem to be necessary</u> in the latest versions):

```php
final readonly class YourCustomTypeMiddlewareCompilerPass implements CompilerPassInterface
{
    public function process(ContainerBuilder $container): void
    {
        $configurationDefinition = $container->getDefinition('doctrine.dbal.default_connection.configuration');

        $setMiddlewaresMethodCallArguments = $this->getSetMiddlewaresMethodCallArguments($configurationDefinition);

        $setMiddlewaresMethodCallArguments[0] = array_merge($setMiddlewaresMethodCallArguments[0] ?? [], [new Reference('your.custom.type.dbal.middleware')]);

        $configurationDefinition
            ->removeMethodCall('setMiddlewares')
            ->addMethodCall('setMiddlewares', $setMiddlewaresMethodCallArguments);
    }

    /** @return array[] */
    private function getSetMiddlewaresMethodCallArguments(Definition $definition): array
    {
        foreach ($definition->getMethodCalls() as $methodCall) {
            if ('setMiddlewares' === $methodCall[0]) {
                return $methodCall[1];
            }
        }

        return [];
    }
}
```