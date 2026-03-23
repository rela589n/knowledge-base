This will include one directory (due to `glob` function):

```php
$files = glob(__DIR__. '/Models/Quote/{,*/}*.php', GLOB_BRACE);
```

An example with configurable nesting:

```php
$depth = 7;
$prefixes = array_map(
    static fn (int $level): string => str_repeat('*/', $level),
    range(1, $depth),
);

$nestingPattern = '{'.implode(',', $prefixes).'}';

/** @var list<string> $glob */
$glob = glob(
    $basePath.sprintf('/%s*Sfx.php', $nestingPattern),
    GLOB_BRACE | GLOB_NOSORT,
);
```
