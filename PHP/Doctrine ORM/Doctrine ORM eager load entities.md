```php
/** @var YourEntity[] $result */
$result = $qb->getQuery()
    ->setFetchMode(YourEntity::class, 'yourRelation', ClassMetadata::FETCH_EAGER)
    ->getResult();
```
