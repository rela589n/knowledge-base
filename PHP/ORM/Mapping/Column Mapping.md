For a Column Mapping we strictly adhere to the principle that the database must constrain the value no more than the type itself. 

For example, this filed is mapped as `bigint`:

```php
#[Column]
private int $seq;
```

This is mapped as `text`:
```php
#[Column]
#[Unique]
private string $email;
```

If you need to have a more constrained database representation, you should create a [[Value Object]], and attach respective mapping there.

```php
#[Column]
private Uuid $id; // mapped as db uuid
```

This kind of mapping is not different from scalar mapping. It offers similar idea to [[PostgreSQL Custom Type|PostgreSQL Domain Types]], which are just nothing else but more restrained underlying types.

### Custom [[Value Object|Value]] Type

Let's say we need to create an imaginary `Char10`:

Client will have it no different from scalar mapping:
```php
#[Column]
private Char10 $str;
```

Type itself must implement [[Business Rule]] and attribute itself with a corresponding SQL-type:

```php
#[FixedCharSqlType(10)]
class Char10
{
    public function __construct(
        #[Target]
        private(set) string $value,
    ) {
        Assert::length($this->value, 10);
    }
}
```

SQL-type is responsible for creating an appropriate SQL declaration and might also do proper value conversion. There're some built-in SQL types.

#### Custom SQL Type

If you need to write custom type, here's how you do it:

```php
#[Attribute(Attribute::TARGET_CLASS)]
class FixedCharSqlType implements SqlType
{
    public function __construct(
        private string $length,
    ) {
    }

    public function getDeclaration(): string
    {
        return sprintf('CHAR(%s)', $this->length);
    }
}
```

