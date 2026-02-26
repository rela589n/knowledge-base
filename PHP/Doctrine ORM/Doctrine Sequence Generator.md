```yaml
services:
    _defaults:
        autowire: true
        autoconfigure: true

    app_your_module.your_sequence.dbal_schema_filter:
        class: Doctrine\Bundle\DoctrineBundle\Dbal\RegexSchemaAssetFilter
        arguments: [ '#^(?!(your_table_seq_id)$).*#' ]
        tags:
            - { name: doctrine.dbal.schema_filter }
```
[[Doctrine Dbal Schema Regex Exclude Filter]]

Then generate:
```php
public const YOUR_SEQUENCE_NAME = 'your_table_seq_id';

public const YOUR_SEQUENCE_ALLOCATION_SIZE = 1;

private SequenceGenerator $sequenceGenerator;

public function __construct(
    private EntityManagerInterface $entityManager,
) {
    $this->sequenceGenerator = new SequenceGenerator(
        self::YOUR_SEQUENCE_NAME,
        self::YOUR_SEQUENCE_ALLOCATION_SIZE,
    );
}

public function generateSeqId(): int
{
    /** @var int $seqId */
    $seqId = $this->sequenceGenerator->generateId($this->entityManager, null);

    return $seqId;
}
```

```php
final class Version20250704055923 extends AbstractMigration
{
    public function up(Schema $schema): void
    {
        $this->addSql('CREATE SEQUENCE your_table_seq_id INCREMENT BY 1 MINVALUE 1 START 1');
    }

    public function down(Schema $schema): void
    {
        $this->addSql('DROP SEQUENCE your_table_seq_id CASCADE');
    }
}
```
