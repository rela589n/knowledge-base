See [[Explicit locking|lock for update]].

```php
class ForUpdateOfTableWalker extends SqlWalker
{
    public const FOR_UPDATE_OF_TABLE = 'ForUpdateOfTable';

    public function walkSelectStatement(SelectStatement $AST): string
    {
        $sql = parent::walkSelectStatement($AST);
        /** @var array $hint */
        $hint = $this->getQuery()->getHint(self::FOR_UPDATE_OF_TABLE);

        $tableAlias = $this->getSQLTableAlias($hint[0], $hint[1]);

        $sql .= ' FOR UPDATE OF '.$tableAlias;

        return $sql;
    }
}

// Repository
        $query = $qb->getQuery();
        $query->setHint(Query::HINT_CUSTOM_OUTPUT_WALKER, ForUpdateOfTableWalker::class);
        $query->setHint(ForUpdateOfTableWalker::FOR_UPDATE_OF_TABLE, ['abstract_entities', 'a']);
```