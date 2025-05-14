Components:
- [[Sorted Array]]
- [[O (log N)]]

There are two ways of implementing binary search:
- iterative
- recursive

```php
/** check on [1, 3, 5, 7] */
function binarySearch(array $nums, int $target)
{
    $n = count($nums);

    $l = 0;
    $r = $n - 1;

    while ($l < $r) {
        $m = $l + (($r - $l) >> 1);

        if ($target < $nums[$m]) {
            $r = $m - 1;
        } elseif ($nums[$m] < $target) {
            $l = $m + 1;
        } else {
            return $m;
        }
    }

    // After the loop $r is less than $l, and $l is greater than $r
    // $l can be from [0 to $n] inclusively
    // $r can be from [-1 to $n - 1] inclusively

    // Table on where pointers end up 
    // for different numbers after the loop:
    // 
    //  [1, 3, 5, 7] 
    // R L            0
    //   R  L         2
    //      R  L      4
    //         R  L   6
    //            R L 8
    //
    // Therefore, after the loop pointers are flipped.

    return -1;
}
```