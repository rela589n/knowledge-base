Memory limit for the [[PHP/Opcache/Shared Memory|Shared Memory]]:
```ini
opcache.memory_consumption = 128M
```

Size of [[Hash Table|Hash Table]], determines the max number of files Opcache could store:
```ini
opcache.max_accelerated_files = 16000
```

Size of interned **strings buffer**:
```ini
opcache.interned_strings_buffer=16
```

[[Opcache Preloading|Preloading]] script:
```ini
opcache.preload=/app/config/preload.php
```

Whether [[PhpDoc]]s should be saved in [[PHP/Opcache/Shared Memory|Shared Memory]]:
```ini
opcache.save_comments = 0
```
