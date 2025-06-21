
```php
function transposeMatrix(array $matrix): array
{
    if (1 === count($matrix)) {
        return array_chunk(reset($matrix), 1);
    }

    return array_map(null, ...$matrix);
}
```