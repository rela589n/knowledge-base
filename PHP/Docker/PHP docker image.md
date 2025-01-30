See https://hub.docker.com/_/php

Docker images could be suffixed with debian linux names.

For instance, debian 12:
```Dockerfile
FROM php:8.3-cli-bookworm
```

Installation of php extensions in docker: 
- `docker-php-ext-install`
- `docker-php-ext-enable`

See:
- [[Composer docker installation]]
- [[PHP ext-pgsql extension docker installation]]
