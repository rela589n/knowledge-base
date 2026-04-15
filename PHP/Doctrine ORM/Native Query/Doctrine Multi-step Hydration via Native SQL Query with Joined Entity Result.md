
```php
$rsm = new ResultSetMappingBuilder($this->getEntityManager());

$rsm->addEntityResult(YourOneEntity::class, 'one');
/* We can't just use your_one_entity_id (FK column) here since RSM thinks that it's related (while really it's not) to your_many_entities.id (see the result of $rsm->generateSelectClause()), resulting in null result set. Thus, avoid it by preventing id collision in RSM.*/
$rsm->addFieldResult('one', 'one_id', 'id');

$rsm->addJoinedEntityFromClassMetadata(YourManyEntity::class, 'many', 'one', 'yourManyEntities');

$nativeQuery = $this->getEntityManager()->createNativeQuery(
    <<<'SQL'
          SELECT your_one_entity_id AS one_id, * FROM your_many_entities many
          WHERE your_one_entity_id IN (:ids)
          SQL,
    $rsm,
);
$nativeQuery->setParameter('ids', $ids, ArrayParameterType::STRING);

$yourOneEntities = $nativeQuery->getResult();
```

> Note that, actually, we could've used `addRootEntityFromClassMetadata`:
> ```php
> $rsm->addRootEntityFromClassMetadata(YourOneEntity::class, 'one', ['id' => 'one_id']);
> ```
> Yet, this is fraught with more collisions if some fields are present in your Many entity named as your One entity, thus it's better to directly specify `addEntityResult()` with a single `addFieldResult()`.

