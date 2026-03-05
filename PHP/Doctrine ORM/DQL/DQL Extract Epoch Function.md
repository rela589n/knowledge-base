```php
/**
 * Implementation of PostgreSQL's EXTRACT(EPOCH FROM ...) for DQL.
 *
 * Usage in DQL: EXTRACT_EPOCH(entity.timestamp)
 * Translates to SQL: EXTRACT (EPOCH FROM entity.timestamp AT TIME ZONE 'UTC')::BIGINT
 */
final class ExtractEpochFunction extends FunctionNode
{
    private Node $dateExpression;

    public function parse(Parser $parser): void
    {
        $parser->match(TokenType::T_IDENTIFIER);
        $parser->match(TokenType::T_OPEN_PARENTHESIS);

        /** @var Node $node */
        $node = $parser->ArithmeticPrimary();
        $this->dateExpression = $node;

        $parser->match(TokenType::T_CLOSE_PARENTHESIS);
    }

    public function getSql(SqlWalker $sqlWalker): string
    {
        return sprintf(
            "(EXTRACT(EPOCH FROM %s AT TIME ZONE 'UTC')::BIGINT)",
            $this->dateExpression->dispatch($sqlWalker),
        );
    }
}
```
