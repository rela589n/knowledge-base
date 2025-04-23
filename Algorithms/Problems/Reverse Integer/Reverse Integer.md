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

This solution is [[O (log N)]], since it would take 10 iterations to reverse `2147483647` number, and it depends on how many times we could divide the number by 10.

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
function reverse(int $x) 
{
    $res = 0;

    $min = -2 ** 31; // -2147483648
    $almostMin = intdiv($min, 10); // -214748364
    $lastMinDigit = $min % 10; // -8

    $max = 2 ** 31 - 1; // 2147483647
    $almostMax = intdiv($max, 10); // 214748364
    $lastMaxDigit = $max % 10; // 7

    while ($x) {
        // [res > 214748364]
        // it means that if we multiply it by 10 (below in the loop),
        // it would overflow, since it will not be within $max limit
        if ($res > $almostMax)  {
            return 0;
        }

        // [res < -214748364]
        // it means, that if we multiply it by 10 (below in the loop),
        // it would overflow, since it will not be within $min limit 
        if ($res < $almostMin) {
            return 0;
        }

        // [res = 214748364, x > 7]
        // it would overflow, since remaining $x part will make it greater than $max
        // (it could be only the last digit that overflows)
        if ($res === $almostMax and $x > $lastMaxDigit) {
            return 0;
        }

        // [res = -214748364, x < -8]
        // it would overflow, since remaining $x part will make it smaller than $min
        // (it could be only the last digit that overflows)
        if ($res === $almostMin and $x < $lastMinDigit) {
            return 0;
        }

        $res = $res * 10 + $x % 10;
        $x = intdiv($x, 10);
    }       

    return $res;
}
```