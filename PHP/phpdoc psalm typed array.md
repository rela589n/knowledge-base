```php
/**
 * @psalm-type UserStruct = array{
 *  id: string,
 *  name: string,
 * }
 */
```

The import it like this:

```php
/**
 * @psalm-import-type UserStruct from User
 */
```