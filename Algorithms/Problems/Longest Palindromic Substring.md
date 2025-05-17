See [problem](https://leetcode.com/problems/longest-palindromic-substring/description/)

Solution checks from every character if it can be extended to build up palindrome:

```php
function longestPalindrome($string) {
    $chars = str_split($string);
    $n = count($chars);
    $optimal = null;
    $maxLen = 0;

    for ($i = 0; $i < $n; ++$i) {
        $ch = $chars[$i];

        $l = $i;
        $r = $i;
        $len = 1;

        while ($r + 1 < $n && $chars[$r + 1] === $ch) {
            ++$len;
            ++$r;
        }

        while ($l > 0 && $r + 1 < $n) {
            if ($chars[$l - 1] !== $chars[$r + 1]) {
                break;
            }

            $len += 2;
            --$l;
            ++$r;
        }

        if ($maxLen < $len) {
            $maxLen = $len;
            $optimal = [$l, $r];
        }
    }

    // ababa

    [$l, $r] = $optimal;

    return implode('', array_splice($chars, $l, $r - $l + 1));
}
```

One caveat is that for strings like `baaaab`, it's necessary to extend central part as much as possible.