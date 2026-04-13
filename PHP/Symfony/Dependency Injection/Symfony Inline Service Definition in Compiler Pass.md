If you need to define inline service in compiler pass, you can just create `new Definition()` and pass it wherever you need.

```php
private function dateIntervalDefinition(string $interval): Definition
{
    return new Definition(DateInterval::class)
        ->setFactory([DateInterval::class, 'createFromDateString'])
        ->setArguments([$interval])
    ;
}
```