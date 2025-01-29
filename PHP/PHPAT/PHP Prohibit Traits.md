[[PHPAT architecture]]

```php
#[TestRule]
public function testTraitsMustNotBeUsed(): Rule  
{  
    return PHPat::rule()  
        ->classes(Selector::AND(Selector::includes('/.*/', true), Selector::NOT(Selector::classname(Kernel::class)), Selector::NOT(Selector::implements(Test::class))))  
        ->shouldNotInclude()  
        ->classes(Selector::all())  
        ->because("It's better to keep away from using traits and use explicit DI without mutability instead");  
}
```

