
Hello internals
I'm wondering if there are any plans for union type casts support.

That's basically what I mean:

```php
function checkItOut(int|float|string $bar)
{
    $foo = (int|float)$bar;
    
    var_dump($foo);
}
```

I assume the behavior should be the same as if we called function having such union type-hint (with a remark that strict types are disabled):

```php
function checkItOut(int|float|string $bar)
{
    $foo = cast($bar);
    
    var_dump($foo);
}

function cast(int|float $bar): int|float
{
    return $bar;
}
```

Best regards,
Yevhen

