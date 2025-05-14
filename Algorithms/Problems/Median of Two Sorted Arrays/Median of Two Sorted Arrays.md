```
[1]
[2]

m = 1.5 // if we have two items, we just return their average

[2]
[1,3]

m = 2

[1,2,3,4,5,6,7]
[8,9,10,11,12]

m = 7

[4,5,6]
[1,2,3]

m = (3+4)/2

[1,3,5,7]
[2,4,6,8,9]
=> [1,2,3,4,5,6,7,8,9]

m = 5

[1]
[2,3,4,5]

=> 3
```

### Brute-force solution with merge

See algorithm to [[Merge sorted arrays]]. 
This solution is [[O (N)]] time and [[O (N)]] space.

```php
function findMedianSortedArrays($nums1, $nums2) {
    $n1 = count($nums1);
    $n2 = count($nums2);

    $arr = $this->mergeSortedArrays($nums1, $nums2);
    $n = count($arr);

    if ($n & 1) {
        // [1,2,3] (3)

        return $arr[intdiv($n, 2)];
    }

    // [1,2,3,4] (4)
    //  0 1 2 3

    return ($arr[intdiv($n, 2)] + $arr[intdiv($n - 1, 2)]) / 2;
}
```

Actually, we don't need to merge them.

Since we only need the two elements in the middle, we can just find them w/o merging the arrays. 

This algorithm uses [[Two pointers]] approach.

```php
function findMedianSortedArrays($nums1, $nums2) {
    $n1 = count($nums1);
    $n2 = count($nums2);
    $n = $n1 + $n2;

    $midN = intdiv($n, 2) + 1;

    $i = 0;
    $j = 0;
    $m1 = $m2 = 0;

    for ($k = 0; $k < $midN; ++$k) {
        $m1 = $m2;

        if ($i < $n1 && $nums1[$i] <= ($nums2[$j] ?? INF)) {
            $m2 = $nums1[$i++];
        } elseif ($j < $n2 && $nums2[$j] <= ($nums1[$i] ?? INF)) {
            $m2 = $nums2[$j++];
        }
    }

    if ($n & 1) {
        // [1,2,3] (3)

        return $m2;
    }

    // [1,2,3,4] (4)
    //  0 1 2 3

    return ($m1 + $m2) / 2;
}
```

### [[Binary Search]]-based solution

The approach is based on splitting arrays into two halves such that *"every item in two left halves must be less than or equal to every item in the two right halves"*.

For example, there are two arrays:

`arr1 = [1,3,5,7]`
`arr2 = [2,4,6,8]`

We'd split them into:

`arr1L = [1,3], arr1R = [5,7]`
`arr2L = [2,4], arr2R = [6,8]`

Therefore, having made this split, it would be possible to take the greatest value (as max of the two last items) of Left sub-arrays, and the smallest value (as a min of the two first items) of the right sub-arrays, and it would be two median items.




