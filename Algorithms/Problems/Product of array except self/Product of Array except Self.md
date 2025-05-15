---
aliases:
  - Array product except self
---
See [problem](https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=leetcode-75)

### Solution 1 - Complement

Components:
- [[Complement]]

Solution is based on [[Full Product or Sum]], that is later used to extract needed [[Complement]] for the resulting value.

The only disclaimer is that it's important to keep track of zeros count, since the logic differs (it's not possible to divide on zero).

```php
function productExceptSelf($nums) {
    $numsNoZeros = array_filter($nums);
    $zerosCount = count($nums) - count($numsNoZeros);

    $product = array_product($numsNoZeros);

    $res = [];

    foreach ($nums as $num) {
        if ($zerosCount === 0) {
            $res[] = $product / $num;
        } elseif ($zerosCount === 1 && $num === 0) {
            $res[] = $product;
        } else {
            $res[] = 0;
        }
    }

    return $res;
}
```

### Solution 2 - affix product

Components:
- [[Wave]]

Another solution, if we are not allowed to use division operator, would be to maintain [[Affix Operation|Prefix Product]] and [[Affix Operation|Suffix Product]] data structures, so that eventually result can be computed as `res[i] = prefixProduct[i - 1] * suffixProduct[i + 1]`.

This is a [[O (N)]] time and [[O (N)]] memory solution.

```php
function productExceptSelf($nums) {
    $prefixProducts = [-1 => 1];

    foreach($nums as $i => $num) {
        $prefixProducts[$i] = $prefixProducts[$i - 1] * $num;
    }

    $suffixProducts = [count($nums) => 1];

    for ($i = count($nums) - 1; $i >= 0; --$i) {
        $suffixProducts[$i] = $suffixProducts[$i + 1] * $nums[$i];
    }

	// 1 2 3 0 3 2 1

	// prefix: 
	// 1 2 6 0 0 0 0

	// suffix:
	// 0 0 0 0 6 2 1

    $results = [];

    foreach($nums as $i => $num) {
        $results[] = $prefixProducts[$i - 1] * $suffixProducts[$i + 1];
    }

    return $results;
}
```

Also, there's a solution that doesn't use extra memory to maintain prefix and suffix products. It computes prefix and suffix on the fly and multiplies the result right away.

The idea is to initialize result array with 1, and then:
1. multiply every item by respective prefix, 
2. and then multiply every item by the respective suffix:

```php
function productExceptSelf($nums) {
    $results = array_fill(0, count($nums), 1);

    $prefix = 1;

    foreach($nums as $i => $num) {
        $results[$i] *= $prefix; // multiply res[i] by last prefix ([i - 1])

        $prefix *= $num;
    }

    $suffix = 1;

    for ($i = count($nums) - 1; $i >= 0; --$i) {
        $results[$i] *= $suffix; // multipy res[i] by last suffix ([i + 1])

        $suffix *= $nums[$i];
    }

    return $results;
}
```

