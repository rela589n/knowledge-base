See [problem](https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=leetcode-75)

The idea is to use [[Two pointers]].
Actually, we just reconstruct needed string from the characters present in the given string. If next character is respective to the expected character of the string, then we shift pointer. Otherwise, we just skip it.

```php
function isSubsequence($s, $t) {
    // ahbgdc
    // a b  c

    // acabc
    // aabc

    if ($s === '') {
        return true;
    }

    $stack = str_split($t);
    $str = str_split($s);

    $offset = 0;

    foreach ($stack as $char) {
        if ($char === $str[$offset]) {
            ++$offset;
        }

        if ($offset >= count($str)) {
            return true;
        }
    }

    return false;
}
```

And solution that uses regex (simpler to grasp). Just build a regex from the needle string so that each character is surrounded with `.*?` pattern (match anything zero or more times), and then use this regex to match the string:

```php
function isSubsequence($s, $t) {
    // ahbgdc
    // a b  c

    // acabc
    // aabc

    $str = str_split($s);

    $regex = '/'.implode('.*?', $str).'/';

    return preg_match($regex, $t);
}
```

> Note: we could've used `.*` (greedy) regex instead of `.*?` (non-greedy), but using non-greedy is better performance-wise.
