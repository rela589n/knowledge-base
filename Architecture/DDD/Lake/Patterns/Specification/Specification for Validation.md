[[Specification]] allows to check if object fulfills some need / suitable for smth.

The actual [[Specification]] object usually exposes a method as `isSatisfied(candidate)` to check on the real object.

```php
class DelinquentInvoiceSpecification implements InvoiceSpecification
{
    public function __construct(
        private CarbonImmutable $currentDate,
    ) {}

    public function isSatisfiedBy(Invoice $candidate): bool 
    {
        $gracePeriod = $candidate->getCustomer()->getPaymentGracePeriod();
        $firmDeadline = $candidate->getDueDate()->addDays($gracePeriod);

        return $this->currentDate->isAfter($firmDeadline);
    }
}
```