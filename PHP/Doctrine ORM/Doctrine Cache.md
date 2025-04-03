---
aliases:
  - Doctrine Metadata Cache
---
There are three configurations for doctrine cache:

- `metadata_cache_driver`
- `query_cache_driver`
- `result_cache_driver`

By default, for `metadata_cache_driver`, doctrine bundle uses [[PhpArrayAdapter]] (see `DoctrineExtension::createMetadataCache()`), that leverages [[Opcache]] shared memory, providing the best performance since the metadata is read-only. Also, it registers warmer service as `doctrine.orm.default_metadata_cache_warmer` that will load doctrine's metadata during [[Symfony Cache warmup|symfony cache warm up]].


