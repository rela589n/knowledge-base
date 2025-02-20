
```php
#[Serializer\DiscriminatorMap(typeProperty: 'type', mapping: [
    FilterType::AND->value => AndFilterDto::class,
    FilterType::OR->value => OrFilterDto::class,
    FilterType::NULL->value => NullFilterDto::class,
    FilterType::SOME_FILTER->value => SomeFilterDto::class,
])]
interface FilterDto
{
}
```