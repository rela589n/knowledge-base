Something awkward happens with these mapping types.

```yaml
doctrine:
    dbal:
        mapping_types:
            tsvector: tsvector_string
        types:
            tsvector_string: App\Support\Doctrine\Type\TsVectorString\TsVectorStringType
```


