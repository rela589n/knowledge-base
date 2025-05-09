See [problem](https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=leetcode-75)

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

