[[PHPAT architecture]]

```php
#[TestRule]
public function testAbstractClassesMustNotBePrefixedWithAbstract(): Rule
{
    return PHPat::rule()
        ->classes(Selector::isAbstract())
        ->shouldBeNamed('/^(?!.*Abstract).*$/', true)
        ->because('Inheritance MUST not be used for code reuse');
}
```