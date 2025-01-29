[[PHPAT architecture]]

```php
#[TestRule]
public function testEnumsMustNotBeSuffixedWithEnum(): Rule
{
    return PHPat::rule()
        ->classes(Selector::isEnum())
        ->shouldBeNamed('/^(?!.*Enum$).*$/', true)
        ->because('Enums, as value objects, MUST have meaningful name');
}
```