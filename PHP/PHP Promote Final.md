[[PHPAT]]

```php
#[TestRule]
public function testConcreteClassesMustNotBeInheritedFrom(): Rule
{
    return PHPat::rule()
        ->classes(Selector::AND(
            Selector::NOT(Selector::isInterface()),
            Selector::NOT(Selector::isAbstract()),
            Selector::NOT(Selector::appliesAttribute(Entity::class)),
        ))
        ->shouldBeFinal()
        ->because('Concrete classes MUST NOT be inherited from. Make sure to declare them as final.');
}
```