
```Dockerfile
RUN install-php-extensions grpc-1.66.0
```

If you use a separate Docker file for building grpc extension, then you can use it later on in your main docker file this way:

```Dockerfile
# Copy grpc-extension binary  
COPY --from=grpc \  
    /usr/local/lib/php/extensions/no-debug-non-zts-20230831/grpc.so \  
    /usr/local/lib/php/extensions/no-debug-non-zts-20230831/grpc.so  
  
# Create docker-php-ext-grpc.ini configuration file  
RUN docker-php-ext-enable grpc
```
