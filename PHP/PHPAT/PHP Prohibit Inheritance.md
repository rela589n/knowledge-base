[[PHPAT]], [[PHP Promote Final]]

```php
#[TestRule]
public function testInheritanceMustNotBeAbused(): Rule
{
    return PHPat::rule()
        ->classes(Selector::AND(
            Selector::NOT(Selector::appliesAttribute(Entity::class)),
            ...array_map(Selector::NOT(...), $this->abusedInheritedClasses()),
        ))
        ->shouldNotExtend()
        ->classes(Selector::all())
        ->because('Inheritance MUST NOT be used where composition is possible');
}

/** @return list<SelectorInterface> */
private function abusedInheritedClasses(): array
{
    return [
        Selector::extends(AbstractMigration::class),
        Selector::extends(BaseKernel::class),
        Selector::extends(Bundle::class),
        Selector::extends(AbstractExtension::class),
        Selector::extends(Command::class),
        Selector::extends(ServiceEntityRepository::class),
        Selector::extends(TestCase::class),
        Selector::extends(Constraint::class),
    ];
}
```