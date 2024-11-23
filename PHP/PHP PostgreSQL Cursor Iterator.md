See [[PHP PostgreSQL Cursor]]

```php
final class NativeQueryChunkedCursorIterator implements IteratorAggregate
{
    private int $chunkSize;
    private PgSqlNativeQueryCursor $cursor;

    public function __construct(int $chunkSize, NativeQuery $query)
    {
        $this->chunkSize = $chunkSize;
        $this->cursor = new PgSqlNativeQueryCursor($query);
    }

    public function getIterator(): Generator
    {
        $fetchQuery = $this->cursor->getFetchQuery($this->chunkSize);

        $totalCount = 0;
        do {
            $itCount = 0;
            foreach ($fetchQuery->toIterable() as $value) {
                yield $totalCount++ => $value;
                ++$itCount;
            }
        } while ($itCount >= $this->chunkSize);

        $this->cursor->close();
    }

    public function __destruct()
    {
        $this->cursor->close();
    }
}
```