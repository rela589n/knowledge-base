For [[Psalm]]:

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

And [[PHPStan]]:

```php
/**
 * @phpstan-type UserAddress array{street: string, city: string, zip: string}
 */
class User
{
	/**
	 * @var UserAddress
	 */
	private $address; // is of type array{street: string, city: string, zip: string}
}
```

And import:

```php
/**
 * @phpstan-import-type UserAddress from User as DeliveryAddress
 */
class Order
{
	/** @var DeliveryAddress */
	private $deliveryAddress; // is of type array{street: string, city: string, zip: string}
}
```