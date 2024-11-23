
[[PostgreSQL Cursor]] abstraction:

```php
use Doctrine\DBAL\Connection;  
use Doctrine\DBAL\Driver\AbstractPostgreSQLDriver as PDOPgSqlDriver;  
use Doctrine\ORM\NativeQuery;

final class PgSqlNativeQueryCursor
{
    private const DIRECTION_NEXT = 'NEXT';
    private const DIRECTION_PRIOR = 'PRIOR';
    private const DIRECTION_FIRST = 'FIRST';
    private const DIRECTION_LAST = 'LAST';
    private const DIRECTION_ABSOLUTE = 'ABSOLUTE'; // with count
    private const DIRECTION_RELATIVE = 'RELATIVE'; // with count
    private const DIRECTION_FORWARD = 'FORWARD'; // with count
    private const DIRECTION_FORWARD_ALL = 'FORWARD ALL';
    private const DIRECTION_BACKWARD = 'BACKWARD'; // with count
    private const DIRECTION_BACKWARD_ALL = 'BACKWARD ALL';

    /** @var NativeQuery */
    private $query;

    /** @var Connection */
    private $connection;

    /** @var bool */
    private $isOpen = false;

    /** @var string */
    private $cursorName;

    public function __construct(NativeQuery $query)
    {
        $this->query = $query;
        $this->connection = $query->getEntityManager()->getConnection();
        $this->cursorName = uniqid('cursor_', false);

        assert($this->connection->getDriver() instanceof PDOPgSqlDriver);
    }

    public function __destruct()
    {
        if ($this->isOpen) {
            $this->close();
        }
    }

    public function getFetchQuery(int $count, string $direction = self::DIRECTION_FORWARD): NativeQuery
    {
        if (!$this->isOpen) {
            $this->openCursor();
        }

        $query = clone $this->query;
        $query->setParameters([]);
        if (
            $direction === self::DIRECTION_ABSOLUTE
            || $direction === self::DIRECTION_RELATIVE
            || $direction === self::DIRECTION_FORWARD
            || $direction === self::DIRECTION_BACKWARD
        ) {
            $query->setSQL(sprintf(
                'FETCH %s %d FROM %s',
                $direction,
                $count,
                $this->connection->quoteIdentifier($this->cursorName)
            ));
        } else {
            $query->setSQL(sprintf(
                'FETCH %s FROM %s',
                $direction,
                $this->connection->quoteIdentifier($this->cursorName)
            ));
        }

        return $query;
    }

    public function close(): void
    {
        if (!$this->isOpen) {
            return;
        }

        $this->connection->executeStatement('CLOSE ' . $this->connection->quoteIdentifier($this->cursorName));
        $this->isOpen = false;
    }

    private function openCursor(): void
    {
        if ($this->query->getEntityManager()->getConnection()->getTransactionNestingLevel() === 0) {
            throw new BadMethodCallException('Cursor must be used inside a transaction');
        }

        $query = clone $this->query;
        $query->setSQL(sprintf(
            'DECLARE %s CURSOR FOR (%s)',
            $this->connection->quoteIdentifier($this->cursorName),
            $this->query->getSQL()
        ));
        $query->execute($this->query->getParameters());

        $this->isOpen = true;
    }
}
```