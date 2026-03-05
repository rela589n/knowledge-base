```php
final class Version20260405123245 extends AbstractMigration
{
    public function getDescription(): string
    {
        return 'Add function index for entities shuffle key sorting';
    }

    public function up(Schema $schema): void
    {
        $this->addSql(<<<'SQL'
            CREATE INDEX idx_entities_shuffle_key ON entities (MOD(((EXTRACT(EPOCH FROM updated_at AT TIME ZONE 'UTC')::BIGINT) * 100), 71));
        SQL);
    }

    public function down(Schema $schema): void
    {
        $this->addSql('DROP INDEX idx_entities_shuffle_key');
    }
}
```

Then in DQL query builder:

```php
/**
 * Applies deterministic pseudo-random shuffling.
 * Query uses the same expression as is in the idx_entities_shuffle_key.
 * It multiplies by 100 to distribute the otherwise sequential result of modulo until 71 (e.g. 69 % 71 = 69; 70 % 71 = 70; etc.)
 */
private function applySortByShuffleKey(QueryBuilder $qb, SortOrder $sortOrder): void
{
    $qb->addSelect('MOD((EXTRACT_EPOCH(e.updatedAt) * 100), 71) AS HIDDEN shuffleKey')
       ->orderBy('shuffleKey', $sortOrder->value);
}
```

[[DQL Extract Epoch Function]]