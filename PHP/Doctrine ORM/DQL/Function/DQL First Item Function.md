---
aliases:
  - DQL First Row
---
```php
/**
 * Implementation of FIRST(subselect) for DQL subqueries.
 *
 * Usage in DQL: FIRST_ITEM(SELECT ...)
 * Translates to SQL: (SELECT ... LIMIT 1)
 */
final class FirstItemFunction extends FunctionNode
{
    private Subselect $subselect;

    public function parse(Parser $parser): void
    {
        $parser->match(TokenType::T_IDENTIFIER);
        $parser->match(TokenType::T_OPEN_PARENTHESIS);
        $this->subselect = $parser->Subselect();
        $parser->match(TokenType::T_CLOSE_PARENTHESIS);
    }

    public function getSql(SqlWalker $sqlWalker): string
    {
        return sprintf('(%s LIMIT 1)', $this->subselect->dispatch($sqlWalker));
    }
}
```

`first_item_function.yaml`:

```yaml
doctrine:
  orm:
    dql:
      string_functions:
        FIRST_ITEM: App\Framework\Doctrine\DQL\First\FirstItemFunction
```

