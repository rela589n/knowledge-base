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

See [[Merge sorted arrays]]

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

Actually, we don't need to merge them. We only need to find two elements of the middle.