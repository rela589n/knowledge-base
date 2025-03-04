This query returns count of users per notification id.

```php
$rsm = new ResultSetMappingBuilder($this->getEntityManager());

$rsm->addScalarResult('id', 'id');
$rsm->addScalarResult('count', 'count');

$query = $this
    ->createQuery(
        <<<SQL
            SELECT notifications.id, COUNT(user_notifications.*) AS count
            FROM notifications
                LEFT JOIN user_notifications ON notifications.id = user_notifications.notification_id
            GROUP BY notifications.id
        SQL,
        $rsm,
    );

/** @var list<array{id: string, count: int}> $results */
$results = $query->getResult();

return $results;
```