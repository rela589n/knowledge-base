
```php
$rsm = new ResultSetMappingBuilder($this->entityManager);

$columns = [
    [
        'column' => 'id',
        'type' => UuidType::NAME,
    ],
    [
        'column' => 'count',
        'type' => Types::INTEGER,
    ],
];

foreach ($columns as $index => ['column' => $columnName, 'type' => $type]) {
    $rsm->addScalarResult($columnName, $index, $type);

    $rsm->newObjectMappings[$columnName] = [
        'className' => RespondentsCountDto::class,
        'objIndex' => 0,
        'argIndex' => $index,
    ];
}

return $rsm;
```