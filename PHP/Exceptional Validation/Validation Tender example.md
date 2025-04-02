Tender Period example (could not change tender because of start date validation that it's greater than now)

For example, in Symfony application we could have `CreateTenderCommand`, and `UpdateTenderCommand`. Both have `TenderPeriodDto` with start date (must be greater than current date), and end date (must be greater than start date). Finally, if we do not think too much about different scenarios, we'll find out that if tender is updated after it has been started, validation won't allow us to update it. 

```php
class TenderPeriodDto
{
    #[Assert\NotBlank]
    #[Assert\DateTime]
    #[Assert\GreaterThan('now')]
    private string $start;

    #[Assert\NotBlank]
    #[Assert\DateTime]
    #[Assert\GreaterThan(propertyPath: 'start')]
    private string $end;
}
```

```php
class CreateTenderCommand
{
    #[Assert\Valid()]
    private TenderPeriodDto $period;

    // @@
}
```

```php
class UpdateTenderCommand
{
    #[Assert\Valid()]
    private TenderPeriodDto $period;

    // @@
}
```
