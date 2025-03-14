Memory limit for the shared memory:
```ini
opcache.memory_consumption = 128M
```

Size of [[Opcache Hash Table|Hash Table]], determines the max number of files Opcache could store:
```ini
opcache.max_accelerated_files = 16000
```

Size of interned strings buffer:
```ini
opcache.interned_strings_buffer=16
```

[[Opcache Preloading|Preloading]] script:
```ini
opcache.preload=/app/config/preload.php
```

Whether [[PhpDoc]] comments should be saved in [[Opcache Shared Memory|shared memory]]:
```ini
opcache.save_comments = 0
```
