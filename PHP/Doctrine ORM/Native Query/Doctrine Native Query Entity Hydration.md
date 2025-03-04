```php
/** @return YourEntity[] */
public function findYourEntities(User $owner): array
{
    $query = $this
        ->getEntityManager()
        ->createNativeQuery(
            <<<'SQL'
            SELECT your_entities.*  
            FROM your_entities  
            WHERE your_entities.deleted_at IS NULL
              AND owner_id = :owner_id  
            SQL,
            $this->buildRsm()
        )->setParameter('owner_id', $owner->getId()->toRfc4122());

    /** @var YourEntity[] $entities */
    $entities = $query->execute();

    return $entities;
}

private function buildRsm(): ResultSetMappingBuilder
{
    $rsm = new ResultSetMappingBuilder($this->getEntityManager());

    $rsm->addRootEntityFromClassMetadata(YourEntity::class, 'section');

    return $rsm;
}
```