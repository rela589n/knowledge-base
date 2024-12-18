These attributes prevent doctrine from creation of the migration that is trying to drop the constraint.

```php
#[ORM\Index(columns: ['schedule_id'], name: 'vacations_non_overlapping_periods')]
#[ORM\Index(columns: ['schedule_id'], name: 'idx_143b5305a40bc2d5')]
```

Another alternative solution would be defining schema listener:

```php
final readonly class VacationNonOverlappingPeriodsConstraintSchemaListener
{
    /** @throws SchemaException */
    public function postGenerateSchema(GenerateSchemaEventArgs $eventArgs): void
    {
        $schema = $eventArgs->getSchema();

        $table = $schema->getTable('vacations');

        $table->addIndex(['schedule_id'], 'vacations_non_overlapping_periods');
        $table->addIndex(['schedule_id'], 'idx_143b5305a40bc2d5');
    }
}
```

