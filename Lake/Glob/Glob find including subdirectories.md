This will include one directory (due to `glob` function):

```php
$files = glob(__DIR__. '/Models/Quote/{,*/}*.php', GLOB_BRACE);
```

An example with configurable nesting:

```php
$depth = 7;
$nestingPattern = str_repeat('{,*/}', $depth);

/** @var list<string> $glob */
$glob = glob(
    $basePath.sprintf('/%s*Sfx.php', $nestingPattern),
    GLOB_BRACE | GLOB_NOSORT,
);
```
