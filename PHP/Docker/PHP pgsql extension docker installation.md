
There's the problem that `docker-php-ext-install` doesn't install all necessary apt dependencies. They must be either installed manually:

```Dockerfile
RUN apt-get install -y libpq-dev \  
 && docker-php-ext-install pgsql
```

Or, as an alternative, [[docker-php-extension-installer]] could be used.