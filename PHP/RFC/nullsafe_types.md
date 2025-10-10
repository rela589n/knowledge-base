

The idea is pretty simple.

Instead of doing this:

```php

class Foo
{
  public ?Bar $bar = null;
}

class Bar
{
  public int $baz;
}

fas($foo->bar?->baz);
tes($foo->bar?->baz);

```

We can remove duplication of question mark in all usage places by making type nullsafe.

```php
class Foo
{
  public ??Bar $bar;
}

class Bar
{
  public int $baz;
}

fas($foo->bar->baz);
tes($foo->bar->baz);

```

Regarding union types:

```php
class Foo
{
  public ?null|Bar $bar;

  public Baz|Tres|?null $res;
}
```

In first case, `?null|Bar` is long form of `??Bar`.
In second one, `Baz|Tres|?null` value of this type can be either Baz or Tres or "safe null". Safe null is basically an pseudo-object, which for any interaction (property acces or method call) returns same "safe null".


For union types, safe null should only be allowed in disjunction with object.

```php
class Foo
{
  // Error
  public ??int $int;
  
  // allowed
  public ??object $o;
  
  // allowed, at least one object
  public ?null|Bar|int|array $val;
}
```

Special attention requires nullsafe mixed value. It doesn't require two question marks, but one, because mixed itself has an null inside.

```php
class Bar
{
  // this is nullsafe mixed value
  public ?mixed $mixed;
}

$bar->mixed->property;
```

> Safe null must behave almost like null. So that $safeNull === null is true. If we would really like to tell apart safe null from null, some helper function may be introduced.


About method calls, this should be allowed:

```php
$resultOrSafeNull = $valueOrSafeNull->someMethod();
```

Using nullsafe operator on nullsafe value should be allowed:

```php
$valueOrSafeNull?->method();
$valueOrSafeNull?->property;
```

Nullsafe type should be allowed as:
- parameter types
- return types
- property types





