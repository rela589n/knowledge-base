This function returns max sum of all subarrays of given size using [[Fixed-size Sliding Window]]:

```php
function getWindowMaxSum(int $size, array $nums): int
{
    $n = count($nums);
    $sum = 0;

    for ($i = 0; $i < $size; ++$i) {
        $sum += $nums[$i];
    }

    $maxSum = $sum;

    for ($i = $size; $i < $n; ++$i) {
        $sum += $nums[$i] - $nums[$i - $size];

        if ($maxSum < $sum) {
            $maxSum = $sum;
        }
    }

    return $maxSum;
}
```