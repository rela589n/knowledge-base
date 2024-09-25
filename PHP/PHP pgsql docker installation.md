
```Dockerfile
RUN apt-get install -y libpq-dev \  
 && docker-php-ext-install pgsql
```
