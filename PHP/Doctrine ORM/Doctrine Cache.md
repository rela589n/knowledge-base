There are three configurations for doctrine cache:

- `metadata_cache_driver`
- `query_cache_driver`
- `result_cache_driver`

By default, for `metadata_cache_driver`, doctrine bundle uses [[PhpArrayAdapter]], that leverages [[Opcache]] shared memory, having the best performance since metadata is read-only cache. Also, it registers warmer service as `doctrine.orm.default_metadata_cache_warmer` that will load doctrine's metadata when [[Symfony Cache warmup|symfony warms up cache]].

