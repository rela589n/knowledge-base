Find [max average subarray](https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=problem-list-v2&envId=sliding-window):

Solution uses [[Sliding Window]] technique.

```php
function findMaxAverage($nums, $k) {
    // the solution finds max sum of all subarrays, 
    // and then returns it divided by k, producing an average

    $maxSum = 0;
    $n = count($nums);

    for ($i = 0; $i < $k; ++$i) {
        $maxSum += $nums[$i];
    }

    $slidingSum = $maxSum;

    for ($i = $k; $i < $n; ++$i) {
        $slidingSum += $nums[$i]- $nums[$i - $k];

        if ($slidingSum > $maxSum) {
            $maxSum = $slidingSum;
        }
    }

    return $maxSum / $k;
}
```