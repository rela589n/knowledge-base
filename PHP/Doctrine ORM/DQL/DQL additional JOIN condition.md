```php
final class FutureDisabledDateFilter extends SQLFilter
{
    public function addFilterConstraint(ClassMetadata $targetEntity, string $targetTableAlias): string
    {
        if (DisabledDate::class !== $targetEntity->getName()) {
            return '';
        }

        return sprintf('%s.date >= CURRENT_DATE', $targetTableAlias);
    }
}
```

Then, configure it in `doctrine.yaml`.

```yaml
doctrine.orm.filters:
	futureDisabledDateFilter:
		class: App\FutureDisabledDateFilter
		enabled: true
```

