```php
function mergeSortedArrays(array $nums1, array $nums2)
{
    $n1 = count($nums1);
    $n2 = count($nums2);

    $arr = [];

    $i = 0;
    $j = 0;

    while ($i < $n1 || $j < $n2) {
        while ($i < $n1 && $nums1[$i] <= ($nums2[$j] ?? INF)) {
            $arr[] = $nums1[$i++];
        }

        while ($j < $n2 && $nums2[$j] <= ($nums1[$i] ?? INF)) {
            $arr[] = $nums2[$j++];
        }
    }

    return $arr;
}
```