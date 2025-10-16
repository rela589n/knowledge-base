---
aliases:
  - Denormalized foreign key
---
Composite [[Foreign Key]]

This is a relatively easy way to keep the denormalized fields up-to-date.

Consider this example, where `category_materialized_path` field from `category` table is added to the  `product` table:

```php
$productTable = $schema->getTable('product');
$productTable->addColumn('category_materialized_path', 'string', ['length' => 255, 'notnull' => false]);

// unique contraint is required on the target table
$queries->addPreQuery(new SqlMigrationQuery(
    <<<'SQL'
        ALTER TABLE category
            ADD CONSTRAINT category_materialized_path_key
                UNIQUE (materialized_path, id)
        SQL
));

$productTable->addForeignKeyConstraint(
    $schema->getTable('category'),
    ['category_materialized_path', 'category_id'],
    ['materialized_path', 'id'],
    ['onDelete' => 'SET NULL', 'onUpdate' => 'CASCADE'],
    'product_category_materialized_path_fkey',
);

$queries->addPostQuery(new SqlMigrationQuery(
    <<<'SQL'
        UPDATE product
        SET category_materialized_path = category.materialized_path
        FROM category
        WHERE category.id = product.category_id
        SQL
));
```

In this example, once [[Foreign Key]] is added, `'onUpdate' => 'CASCADE'` will take care of [[Foreign Key]] updates.

> You are to use this approach wisely, since it works well **only for NOT NULL fields**. 
> 
> If it is really needed to work with nullable fields, see [[Composite nullable foreign key fix trigger]]


