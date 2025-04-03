---
aliases:
  - Doctrine exclude table from schema
---


```yaml
app_your_project.dbal.schema_filter:
    class: Doctrine\Bundle\DoctrineBundle\Dbal\RegexSchemaAssetFilter
    arguments: [ '#^(?!(your_table_id_seq)$).*#' ]
    tags:
        - { name: doctrine.dbal.schema_filter }

```