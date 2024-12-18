```php
#[AsDoctrineListener(event: ToolEvents::postGenerateSchema)]
final readonly class QuestionForeignKeyListener
{
    /** @throws SchemaException */
    public function postGenerateSchema(GenerateSchemaEventArgs $eventArgs): void
    {
        $schema = $eventArgs->getSchema();

        $table = $schema->getTable('answers');

        $table->addForeignKeyConstraint('questions', ['question_id'], ['id'], name: 'your_custom_foreign_key');
    }
}
```