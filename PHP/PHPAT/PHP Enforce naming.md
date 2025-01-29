[[PHPAT architecture]]

### Api points

```php
#[TestRule]
public function testApiPointsMutBeNamedRespectively(): Rule
{
    return PHPat::rule()
        ->classes(Selector::appliesAttribute(AsController::class))
        ->shouldBeNamed('/(FrontendApiPoint|AnotherApiPoint)$/', true);
}
```

### Console commands

```php
#[TestRule]
public function testConsoleCommandsMustBeNamedRespectively(): Rule
{
    return PHPat::rule()
        ->classes(
            Selector::extends(ConsoleCommand::class),
            Selector::appliesAttribute(AsCommand::class),
        )
        ->shouldBeNamed('/.*ConsoleCommand$/', true)
        ->because('Every console command MUST be named as ConsoleCommand');
}
```

### Fixtures

```php
#[TestRule]
public function testFixturesMustBeNamedRespectively(): Rule
{
    return PHPat::rule()
        ->classes(Selector::implements(FixtureInterface::class))
        ->shouldBeNamed('/Fixture$/', true);
}
```


