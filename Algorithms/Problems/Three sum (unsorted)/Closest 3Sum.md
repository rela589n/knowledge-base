See [problem](https://leetcode.com/problems/3sum-closest/description/).

Need to find 3sum, closest to given target.

### [[Sorting]] and [[Two pointers]]

```php
function threeSumClosest($nums, $target) {
    sort($nums);

    $minSumDiff = INF;
    $closestSum = -1;

    // target = 10
    // sum = 4
    // diff = 10 - 4 = 6

    // sum = -1
    // diff = 10 + 1 = 11
    
    // sum = 8
    // diff = 10 - 8 = 2 (closest sum is 8)

    for ($i = 0, $n = count($nums); $i < $n - 2; ++$i) {

        $first = $nums[$i];
        $j = $i + 1;
        $k = $n - 1;

        while ($j < $k) {
            $second = $nums[$j];
            $third = $nums[$k];

            $sum = $first + $second + $third;

            // we must use abs, since otherwise [11, 12] would produce -1, while [11, 11] (more correct answer) - 0, leading to -1 being accepted as the answer
            $sumDiff = abs($target - $sum);

            // we are finding such $sum that is the least in difference with $target (finding min by sum diff)
            if ($sumDiff < $minSumDiff) {
                $minSumDiff = $sumDiff;
                $closestSum = $sum;
            }

            // [-4,-1,1,2] target = 1
            //  -4      2 => -2
            //     -1   2 => -1
            //        1 2 => 3
            // moving up to the target
            if ($sum < $target) {
                ++$j;
            } elseif ($sum > $target) {
                --$k;
            } else {
                // found perfect sum that matches target

                break 2;
            }
        }

		while ($first === $nums[$i + 1] && $i < $n - 2) 
		{
	        ++$i;
	    }
    }

    return $closestSum;
}
```
