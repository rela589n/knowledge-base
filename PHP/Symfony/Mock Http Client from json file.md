
```php
final readonly class services implements CompilerPassInterface
{
    public function __invoke(ContainerConfigurator $container, ContainerBuilder $builder): void
    {
        if ('test' !== $container->env()) {
            return;
        }

        $builder->addCompilerPass($this);

        $this->addStubClientDefinition($container->services());
    }

    public function process(ContainerBuilder $container): void
    {
        $gatewayDefinition = $container->getDefinition(YourGateway::class);

        $gatewayDefinition->setArgument('$httpClient', new Reference(YourGateway::class.'.http_client.stub'));
    }

    private function addStubClientDefinition(ServicesConfigurator $services): void
    {
        $services
            ->set(YourGateway::class.'.http_client.stub', MockHttpClient::class)
            ->args([
                inline_service(JsonMockResponse::class)
                    ->factory([JsonMockResponse::class, 'fromFile'])
                    ->args([__DIR__.'/exampleData.json']),
            ]);
    }
}

return (new services())(...);
```