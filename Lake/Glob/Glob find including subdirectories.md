This will include one directory (due to `glob` function):
```php
$files = glob(__DIR__. '/Models/Quote/{,*/}*.php', GLOB_BRACE);
```
