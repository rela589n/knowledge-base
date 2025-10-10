
## Approach 1

When using strict_types, everything is obvious (thow error if there's no exact signature).

```
declare(strict_types=1);

class Money
{
	public function plus(self $other);
	
	public function plus(int $other);
}

$money->plus(true); // error
```

Implicit cast from int to float is allowed:

```
declare(strict_types=1);

class Foo
{
	public function bar(bool $a, int $b);

	public function bar(int $a, float $b);
}

$foo->bar(12, 34);
// this will call `bar(int $a, float $b)`
```

When not using strict_types, things become a bit more complicated.

```
class Foo
{
	public function bar(int $a, float $b);

	public function bar(int $a, int $b);
}

$foo->bar(123, true);
```

Algorithm:

1. If there's only one overloaded method with such number of arguments as provided, then we simply call it and cast all the arguments provided with semantics of PHP.

```
public function bar(int $a, float $b, string $c);
public function bar(int $a, float $b);
public function bar(int $a, int $b);

$o->bar(1,2,3); // only one matching method with 3 arguments
```

2. If there're multiple methods with same count of arguments as provided, then analyse them from left-to-right. One by one reduce "list of probable methods" until there's only one.

2.1 Currently analysed argument has matching type declaration

```
public function sum(int $a, int $b): int;
public function sum(float $a, float $b): float;
```

Which function would `sum(17.4, 42)` call?

This will call `sum(float $b, float $b)`, because first parameter matched signature reducing "list of probable methods" to single method. Second argument 42 will be casted to 42.0

2.2 Currently analysed argument has not exact type declaration, but there's overloaded method accepting parameter of union type containing exact type.

```
public function foo(int $a, int $b): int;
public function foo(float $a, float $b): float;
public function foo(string|bool $a, string $b): void;
public function foo(string|bool $a, bool|int $b): void;
```

Which function would `foo(false, true)` call?
This will call `foo(string|bool $a, bool|int $b)`, because first parameter matched union type (string|bool) thus reducing "list of probable methods" to last two methods. And again, second parameter matches union type (bool|int).


2.3 Currently analysed argument has not exact type declaration, no exact union type, but there's overloaded method accepting `mixed` (no type-declaration)

```
public function bar(int $a, int $b): int;
public function bar(float $a, float $b): float;
public function bar($a, string $b): void;
```

Which function would `bar("string", 42)` call?
This will call `bar($a, string $b)`, because there's no method with (string) first parameter, but is method with (mixed) one. Second parameter will be casted into string.

2.4 Currently analysed parameter has not exact type declaration at all and has to be casted.

```
public function foo(bool $a, int $b): int;
public function foo(string $a, float $b): float;
```

Which function would `foo(123, 345)` call?

This will call `foo(string $a, float $b)`.

The way it works is really similar to how union types does.

First argument (int) has to be passed into (bool|string).

If argument's type is not present in signature, then the following priorities apply:
- int
- float
- string
- bool

Generally saying this should use union types semantics `https://wiki.php.net/rfc/union_types_v2`.

Conversion Table:

| Original type |	1st try  |	2nd try  |	3rd try  |
|---------------|------------|-----------|-----------|
| `bool`        | `int`      | 	`float`  |	`string` |
| `int`         | `float`    | 	`string` |	`bool`   |
| `float`       | `int`      | 	`string` |	`bool`   |
| `string`      | `int/float`| 	`bool`   |           |
| `object`      | `string`   |           |           |


```
public function foo(int $a, float $b): void;
public function foo(int $a, bool $b): void;
public function foo(float $a, int $b): void;
```

`foo(true, "123")` will call `foo(int $a, float $b)`:

First parameter (bool) has to be casted into (int|float). Integer has greater priority, than float, thus "list of probable methods" is reduced to [`foo(int $a, float $b)`, `foo(int $a, bool $b)`]. The next parameter (string) has to be casted into (float|bool). Thus, float is selected, because it is numeric string.


Another example with union types:
```
public function foo(int $a, float $b): void;
public function foo(float|bool $a, int $b): void;
```

Which function would `foo("string", 123.45)` call?

This will call `foo(float|bool $a, int $b)` with `$a=true` and `$b=123`.

How this works:
First parameter (string) has to be casted into (int|(float|bool)). In accordance with table above, string 1st try is `int/float`. It can't be casted into `int`. Then we check whether it could be casted into (float/bool). Into float it can't be casted (again, not numeric string). Thus, cast it into `bool`.

Restrictions of this approach:

Union types, which partically covers other method's parameter even if other parameters have different types.

In example below `int|float` logically acts only as `float`. 
Call `foo(1, "string")` will call first method, though client code probably expects second to be executed:

```
public function foo(int $a, bool $b): void;
public function foo(int|float $a, string $b): void;
```

## Approach 2

The key difference from first approach is in case when there're set of methods with same number of parameters and we have to choose one of them.

The main idea is next: analyse parameters all together and for every method calculate "match rate". 

```
public function foo(int $a, int $b, bool $c): void;
public function foo(float $a, float $b, string $c): void;
```

`foo(12, 34.56, 'string');`
This will call `foo(float $a, float $b, string $c)`.

`foo(12, 34.56, true);`
This will call `foo(int $a, int $b, bool $c)`.

How "match rate" is calculated:

methods list = all overloaded methods with such number of parameters

If given arguments have objects, then:
  remove items from methods list where object can't be casted into expected argument
  # for example: (string) is expected, but (Object) doesn't implement `Stringable`

Loop over methods list:

  Loop over each passed argument and:
    If expected is object (or part of union) of provided type then:
	  increase "match rate" of this method by 32768
    Else If expected type is exactly as given (or exactly in union):
	  increase "match rate" of this method by 512
	Else If expected type is `mixed` (no type-hint) then:
	  increase "match rate" of this method by 504
	
	Else If given type present in table:
	  | Given type \ Expected  | int | float | string |
      |------------------------|-----|-------|--------|
      | `int`                  | 512 | 512   | 2      |
      | `string_numeric`       | 512 | 512   | 511    |
	  foo(bool, bool) 3 + 512
	  foo(int, int) 512 + 2 = 514
	  foo(string, float) 510 + 2 = 512
	  
	  foo("123", true)
	  
	  foo(bool, bool) 1 + 512
	  foo(int, int)  3 + 2
	  foo(string, float) 
	 
	  foo(123.45, true) 
    Else:
	  do not do anything.
Sort (using stable algorithm) list of methods by their "match rate".

If first method from list has greater "match rate" than second, then:
   select first one as most matching. DONE   
Else:
  LogicException, we didn't manage some case.
  
```
public function foo(string $a, int $b): void;
public function foo($a, float $b): void;
```

foo(1,2);

1 => 32
2 => 30 + 32 = 62


```
public function foo(A $a, int $b, int $c): void;
public function foo(string $a, bool $b, bool $c): void;
```

32 + 27 + 27
26 + 32 + 32
foo(new A, true);