
```php
    /** @var YourOneEntity[] $oneEntities */
    $oneEntities = $qb->getQuery()->getResult();

    if ([] === $oneEntities) {
        return $oneEntitites;
    }

    $oneEntityIds = array_map(static fn (YourOneEntity $oneEntity): string => $oneEntity->getId()->toRfc4122(), $oneEntities);

    $this->preloadManyEntities($oneEntityIds);

    return $oneEntities;
@@

/** @param string[] $oneEntityIds */
private function preloadManyEntities(array $oneEntityIds): void
{
    $nativeQuery = $this->getEntityManager()->createNativeQuery(
    // Note: one.id must be the first selected clause (RSM won't map collection otherwise)
        <<<'SQL'
              SELECT one.id AS one_id, many.*
              FROM your_one_entities one
                  LEFT JOIN your_many_entities many ON many.your_one_entity_id = one.id
              WHERE one.id IN (:ids)
              SQL,
        $this->manyEntitiesRSM(),
    );
    $nativeQuery->setParameter('ids', $oneEntityIds, ArrayParameterType::STRING);
    $nativeQuery->execute();
}

private function manyEntitiesRSM(): ResultSetMappingBuilder
{
    $rsm = new ResultSetMappingBuilder($this->getEntityManager());

    $rsm->addEntityResult(YourOneEntity::class, 'one');
    // Note: we can't just use your_one_entity_id since RSM confuses it for many.id (see the result of $rsm->generateSelectClause())
    $rsm->addFieldResult('one', 'one_id', 'id');

    $rsm->addJoinedEntityFromClassMetadata(YourManyEntity::class, 'many', 'one', 'yourManyEntities');

    return $rsm;
}
```

> Note that, actually, we could've used `addRootEntityFromClassMetadata`:
> ```php
> $rsm->addRootEntityFromClassMetadata(YourOneEntity::class, 'one', ['id' => 'one_id']);
> ```
> Yet, this is fraught with more collisions if some fields are present in your Many entity named as your One entity, thus it's better to directly specify `addEntityResult()` with a single `addFieldResult()`.

