See [problem](https://leetcode.com/problems/median-of-two-sorted-arrays/description/)

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

Since we only need the two elements in the middle, we can simply find them w/o merging the arrays. 

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

The approach is in splitting arrays into two equal halves such that *"every item in two left halves is less than or equal to every item in the two right halves"*.

For example, for these two arrays:

`arr1 = [1,3,5,7]`
`arr2 = [2,4,6,8]`

We'd split them into:

`[1,3,| 5,7]`
`[2,4,| 6,8]`

In this example every item keeps the condition:
- `arr1Left <= arr2Right`;
- `arr2Right <= arr1Left`.

The common size of two split pairs on the left and on the right must be equal.

Therefore, having made this split, it is possible to take the greatest value (as max of the two last items) of the Left sub-arrays, and the smallest value (as a min of the two first items) of the right sub-arrays, and these would be two median items.

```
N = 8

[1,3,4,| 7]     (partition1Length=3)
[2,    | 5,6,8] (partition2Length=1)
```

```
N = 5

[1,2,| 3]   (partition1Length=2)
[      4,5] (partition2Length=0)
```

The following condition must always be kept:
`partition1Length + partition2Length = N / 2`, since array must be divided exactly into two equal parts (so that we'd be able to find the median).


1,***3***,4,7
2,***5***,6,8

1,2
3,4
