This listener prevents generation of migration that is trying to drop the constraint.

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