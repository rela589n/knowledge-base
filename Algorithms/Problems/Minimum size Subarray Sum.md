See [problem](https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=problem-list-v2&envId=sliding-window).

Using [[Sliding Window]].

```php
function minSubArrayLen($target, $nums) {
    $n = count($nums);

    // [2,3,1,2,4,3]        
    // we keep increasing the window until we reach target, 
    // then we decrease the window until we stop reaching the target

    $minimalLength = INF;

    $l = 0; // l is inclusive
    $r = 0; // r is exclusive
    $currentSum = 0;

    do {
        while ($currentSum < $target && $r < $n) {
            $currentSum += $nums[$r];

            ++$r;
        }

        while ($currentSum >= $target && $l < $r) {
            $length = $r - $l;

            if ($length < $minimalLength) {
                $minimalLength = $length;
            }

            $currentSum -= $nums[$l];

            ++$l;
        }
    } while ($r < $n);

    if ($minimalLength === INF) {
        return 0;
    }

    return $minimalLength;
}
```