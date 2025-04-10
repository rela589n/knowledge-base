It's possible to call grandparent constructor, given that class extends from it:

```php
class EmailValidationFailedException extends ValidationFailedException
{
    public function __construct(string $email, ?Throwable $previous = null)
    {
        parent::__construct($email);

        Exception::__construct('email validation failed', previous: $previous);
    }
}
```

