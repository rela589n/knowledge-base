This **will not work**:

```php
$qb
    ->where('t INSTANCE OF :type')
    ->setParameter('type', ConcreteType::class);
```

what you should do instead is this:

```php
$qb
    ->where(strtr('t INSTANCE OF :type', [':type' => ConcreteType::class]));
```

Using `strtr` you replace `:type` with the actual type to be used in query.
