```php
#[ORM\Embeddable]
final readonly class InventoryPeriod
{
    private function __construct(
        #[ORM\Column]
        private DateTimeImmutable $startDate,
        #[ORM\Column]
        private DateTimeImmutable $endDate,
    ) {
    }

    public static function betweenDates(DateTimeImmutable $startDate, DateTimeImmutable $endDate): self
    {
        if ($startDate <= new DateTimeImmutable()) {
            throw new InvalidArgumentException('Start date must be greater than the current date');
        }

        if ($endDate <= $startDate) {
            throw new InvalidArgumentException('End date must be greater than the start date');
        }

        return new self($startDate, $endDate);
    }

    public function getStartDate(): DateTimeImmutable
    {
        return $this->startDate;
    }

    public function getEndDate(): DateTimeImmutable
    {
        return $this->endDate;
    }
}
```