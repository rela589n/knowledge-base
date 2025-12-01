
```php
  /**
   * @param array<array-key,mixed> $config
   *
   * @override
   *
   * @throws Exception
   */
  public function load(array $configs, ContainerBuilder $container): void
  {
      /** @var ?string $env */
      $env = $container->getParameter('kernel.environment');

      $loader = new YamlFileLoader($container, new FileLocator(), $env);
      $loader->load(__DIR__.'/../../Unwrapper/services.yaml');

      if (class_exists(AmpCompositeException::class)) {
          $loader->load(__DIR__.'/../../Unwrapper/Amp/services.yaml');
      }

      if (interface_exists(MessengerCompositeException::class)) {
          $loader->load(__DIR__.'/../../Unwrapper/Messenger/services.yaml');
      }
  }
```