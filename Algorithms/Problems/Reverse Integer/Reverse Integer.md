See [problem](https://leetcode.com/problems/reverse-integer/description/).

The idea is that we take modulo by 10 from the original number on every step of iteration, and add it to the multiplied by ten result.

In other words

```php
while ($x) {
  $res = $res * 10 + $x % 10;
  $x = intdiv($x, 10);
}
```

This would produce correct reversed integer.

In order to check that it doesn't overflow range of `[-2 ** 31, 2 ** 31 - 1]`, we should consider res on the previous iteration until it gets to `+- 2 ** 31`.

### Positive: 

  > `2 ** 31 - 1 = 2147483647`
  
#### Success scenario: 

| res       | x   |
| --------- | --- |
| 214748364 | 7   |

It doesn't overflow, since it produces  2147483647, being at the limit of the type.
#### Overflow scenarios:

| res       | x   | comment                       |
| --------- | --- | ----------------------------- |
| 214748364 | 8   | res == 214748364, and x > 7   |
| 214748365 | 1   | res > 214748364, and x is any |

### Negative

> `-2 ** 31 = -2147483648`

#### Success scenario: 

| res        | x   |
| ---------- | --- |
| -214748364 | -8  |

It doesn't overflow, since it produces  -2147483648, being at the limit of the type.

#### Overflow scenarios:

| res        | x   | comment                        |
| ---------- | --- | ------------------------------ |
| -214748364 | -9  | res == -214748364, and x < -8  |
| -214748365 | -1  | res < -214748364, and x is any |

## Solution

This solution combines the initial approach to reverse the integer, and aforementioned checks.

```php
while ($x) {
    if ($res === 214748364 and $x > 7) {
        return 0;
    }

    if ($res > 214748364) {
        return 0;
    }

    if ($res === -214748364 and $x < -8) {
        return 0;
    }

    if ($res < -214748364) {
        return 0;
    }

    $res = $res * 10 + $x % 10;
    $x = intdiv($x, 10);
}

return $res;
```

### Modulos

We could improve it by adding modulo checks.

