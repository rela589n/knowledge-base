

Drop methods:
- `getName`
- `requiresSQLCommentHint`

```diff
-    #[Override]
-    public function getName(): string
-    {
-        return self::NAME;
-    }
-
-    #[Override]
-    public function requiresSQLCommentHint(AbstractPlatform $platform): bool
-    {
-        // this is required to make doctrine migrations diff command
-        // not to generate alter column statement every time
-        return true;
-    }
```

Remove comment from column:

```php
$this->addSql(<<<'SQL'
    COMMENT ON COLUMN users.secret_key IS ''
SQL);
```

Make sure that the current SQL declaration is compatible with the old (e.g. length part, or what not):

```diff
    #[Override]
    public function getSQLDeclaration(array $column, AbstractPlatform $platform): string
    {
+       $column['length'] ??= 255;

        return $platform->getStringTypeDeclarationSQL($column);
    }
```

