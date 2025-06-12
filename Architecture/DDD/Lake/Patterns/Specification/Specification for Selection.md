[[Specification]] allows to select particular object from collection / storage by given Criteria.

```php
class DelinquentInvoiceSpecification implements InvoiceSpecification
{
    public function __construct(
        private CarbonImmutable $currentDate,
    ) {}

    public function asQueryBuilder(QueryBuilder $qb): QueryBuilder
    {
        return (clone $qb)
            ->join('invoice.customer', 'customer')
            ->andWhere(
                $qb->expr()->lt(
                    "DATE_ADD(invoice.dueDate, customer.paymentGracePeriod, 'DAY')",
                    ':currentDate'
                )
            )
            ->setParameter('currentDate', $this->currentDate);
    }
}
```

Or even like this, to keep all in respective places:

```php
// Delinquency rule is defined as:
//    "grace period past as of current date"

return $repository->whereGracePeriodPast($this->currentDate);
```
