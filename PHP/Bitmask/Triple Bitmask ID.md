This class represents way to store three ids in one 64-bit number:

```php
final class TripleBitmaskId
{
    public const FIRST_ID_SHIFT = 64 - self::FIRST_ID_SIZE;
    public const SECOND_ID_SHIFT = 64 - self::FIRST_ID_SIZE - self::SECOND_ID_SIZE;
    public const THIRD_ID_SHIFT = 64 - self::FIRST_ID_SIZE - self::SECOND_ID_SIZE - self::THIRD_ID_SIZE;

    private const FIRST_ID_MASK = 0b0111111111111111111111111111111111110000000000000000000000000000|PHP_INT_MIN;
    private const SECOND_ID_MASK = 0b0000000000000000000000000000000000001111111111111111111100000000;
    private const THIRD_ID_MASK = 0b0000000000000000000000000000000000000000000000000000000011111111;

    private const FIRST_ID_SIZE = 36;
    private const SECOND_ID_SIZE = 20;
    private const THIRD_ID_SIZE = 8;

    private int $id;

    public function __construct(int $id)
    {
        $this->id = $id;
    }

    public static function create(int $id): self
    {
        return new self($id);
    }

    public function firstId(): int
    {
        return (self::FIRST_ID_MASK & $this->id) >> self::FIRST_ID_SHIFT;
    }

    public function secondId(): int
    {
        return (self::SECOND_ID_MASK & $this->id) >> self::SECOND_ID_SHIFT;
    }

    public function thirdId(): int
    {
        return (self::THIRD_ID_MASK & $this->id) >> self::THIRD_ID_SHIFT;
    }
}
```
