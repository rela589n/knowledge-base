```php
private function joinJoinedEntity(QueryBuilder $queryBuilder): void
{
    if (in_array('joinedEntity', $queryBuilder->getAllAliases(), true)) {
        return;
    }

    $mainEntityAlias = $queryBuilder->getRootAliases()[0];

    $joinedEntityIdSubQuery = $queryBuilder->getEntityManager()
        ->createQueryBuilder()
        ->select('firstJoinedEntity.id')
        ->from(JoinedEntity::class, 'firstJoinedEntity')
        ->andWhere(sprintf('firstJoinedEntity.mainEntity = %s', $mainEntityAlias))
        ->orderBy('firstJoinedEntity.id', Order::Descending->value);

    $queryBuilder->leftJoin(
        JoinedEntity::class,
        'joinedEntity',
        Join::WITH,
        condition: sprintf('joinedEntity.id = FIRST_ITEM(%s)', $joinedEntityIdSubQuery->getDQL()),
    );
}
```

It uses [[DQL First Item Function]]