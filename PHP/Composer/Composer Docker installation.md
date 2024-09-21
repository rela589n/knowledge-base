The easiest way to install composer in docker environment is to use additional `FROM`:

```diff
+FROM composer:2.7 AS composer  
FROM php:8.3-cli-bookworm

+COPY --from=composer /usr/bin/composer /usr/local/bin/composer
```
