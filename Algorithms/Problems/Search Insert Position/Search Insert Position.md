See [problem](https://leetcode.com/problems/search-insert-position/)

Solution uses [[Binary Search]] to find the first index where element could've been.

```php
function searchInsert($nums, $target) {
    $l = 0;
    $r = count($nums) - 1;

    while ($l <= $r) {
        $m = $l + intdiv($r - $l, 2);

        $num = $nums[$m];

        //  0 1 2 3 4 5
        // [1,2,3,4,5,6] 1
        //      m (shifting to the left)
        if ($target < $num) {
            $r = $m - 1;
        } elseif ($target > $num) {
            $l = $m + 1;
        } else {
            return $m;
        }
    }

    // if it was not found, then left pointer will be greater than right (l > r)
    // therefore we could return l, since it's the first pointer after the first number that is less than target

    return $l;
}
```

Note that we could not return `$m + 1`, since it would mean that returned value is at least 1, while it could be 0 (for example, `[1,2]` and `target=0`, we'd insert it at 0 position).
