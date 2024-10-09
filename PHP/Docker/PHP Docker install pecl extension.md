When installing pecl extension, it's necessary to enable it afterwards:

```Dockerfile
RUN pecl install grpc-1.66.0 \  
    && docker-php-ext-enable grpc
```
