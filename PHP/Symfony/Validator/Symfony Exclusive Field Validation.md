---
aliases:
  - Symfony validate only one field presence among number of them
---

```php
final readonly class ContactDto
{
    #[Assert\Sequentially(constraints: [
        new Assert\Expression(
            expression: 'this.isExclusiveValue("emailAddress")',
            message: 'email_address_and_phone_number_are_mutually_exclusive',
        ),
        new Assert\Email(),
    ])]
    private ?string $emailAddress;

    #[Assert\Sequentially(constraints: [
        new Assert\Expression(
            expression: 'this.isExclusiveValue("phoneNumber")',
            message: 'email_address_and_phone_number_are_mutually_exclusive',
        ),
        new AssertPhoneNumber(),
    ])]
    private ?string $phoneNumber;

    public function __construct(?string $emailAddress, ?string $phoneNumber)
    {
        $this->emailAddress = $emailAddress;
        $this->phoneNumber = $phoneNumber;
    }

    /** @api - used in #[Assert\Expression] */
    public function isExclusiveValue(string $propertyName): bool
    {
        $provided = array_filter([
            'emailAddress' => $this->emailAddress,
            'phoneNumber' => $this->phoneNumber,
        ], static fn (mixed $value): bool => null !== $value);

        if (!isset($provided[$propertyName])) {
            return true;
        }

        return count($provided) <= 1;
    }
}
```
