Way to get object static method called on.

```php
public static make(int $param)
{
  return (clone $static)->withParam($param);
}
```
