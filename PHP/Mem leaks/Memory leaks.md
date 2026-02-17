[[PHP test garbage collection|PHP memory leak test]]

See:
- https://www.youtube.com/watch?v=56I5C0NYjv8
- meminfo to check what classes leak memory (https://github.com/BitOne/php-meminfo)
- [[Opcache Leaks]]
- [[CacheTool]]

## php-meminfo

### Detect memory usage

```php
$output->writeln(
    sprintf(' Memory usage: %d (%d MB)',
    memory_get_usage(true),
    (int)(memory_get_usage(true) / 1024 / 1024)),
);
```

#### Install extension

```Dockerfile
RUN git clone https://github.com/BitOne/php-meminfo.git /tmp/php-meminfo \
    && cd /tmp/php-meminfo/extension \
    && phpize \
    && ./configure --enable-meminfo \
    && make \
    && make install \
    && echo "extension=meminfo.so" > /etc/php/8.1/mods-available/meminfo.ini \
    && phpenmod meminfo \
    && rm -rf /tmp/php-meminfo
```

### Dump memory file after few leaks

```php
if (!$written && memory_get_usage(true) > 136839168) {  
    $written = true;  
  
    $fp = fopen('/app/meminfo.json', 'w');  
    meminfo_dump($fp);  
    fclose($fp);  
}
```

### Analyse the file

```shell
./bin/analyzer summary /app/meminfo_clean.json | less
```

#### Fix encoding

You might encounter encoding errors. Convert the file:

```shell
php -r "file_put_contents('/app/meminfo_clean.json', mb_convert_encoding(file_get_contents('/app/meminfo.json'), 'UTF-8',
  'UTF-8'));"
```


### More

Read the [doc](https://github.com/BitOne/php-meminfo/blob/master/doc/hunting_down_memory_leaks.md).

### Easy-fix

It's possible that you need to use `@`