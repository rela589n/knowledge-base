It's not possible to implement this kind of relationship:

```php
class User
{
    private string $email;
}
```

```php
class Subscription
{
    // referenced by unique users.email column
    private User $user;
}
```
