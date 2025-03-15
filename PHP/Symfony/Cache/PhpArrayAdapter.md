https://symfony.com/doc/current/components/cache/adapters/php_array_cache_adapter.html

Since [[Opcache]] caches scripts, this is real-fast solution for immutable data. Data is written once, and should never change.

Compared to [[PhpFilesAdapter]], this adapter isn't well suited for write operations, except there's second adapter in the chain.

