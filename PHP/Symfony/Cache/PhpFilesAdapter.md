---
docs:
  - https://symfony.com/doc/current/components/cache/adapters/php_files_adapter.html
---
Really fast adapter that leverages [[Opcache]], and stores cache in different PHP files (one file per value).

You can use it as `cache.adapter.system` 
(see `AbstractAdapter::createSystemCache()`).
