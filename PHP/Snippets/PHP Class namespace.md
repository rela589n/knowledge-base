```php
/**
 * @param non-empty-string $class
 *
 * @return non-empty-string
 */
function class_namespace(string $class): string
{
    /** @var non-empty-list<string> $namespaceParts */
    $namespaceParts = array_slice(explode('\\', $class), 0, -1);

    return implode('\\', $namespaceParts);
}
```
