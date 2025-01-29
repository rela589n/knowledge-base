[[PHPAT architecture]]

```php
#[TestRule]
public function testInterfacesMustNotHaveInterfaceSuffix(): Rule
{
    return PHPat::rule()
        ->classes(Selector::isInterface())
        ->shouldBeNamed('/^(?!.+Interface$).*/', true)
        ->because('You should not have artificial interfaces');
}
```