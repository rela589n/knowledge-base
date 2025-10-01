See [problem](https://leetcode.com/problems/3sum-closest/description/).

Need to find triplet sum, closest to the given target.

### [[Sorting]] and [[Two pointers]]

It's  [[O (N**2)]].

See [[Two Sum (Pair Sum) In sorted Array]].

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

            // Must use abs, lest [11, 12] will produce -1, while [11, 11] is more correct answer - 0. Closest means by modulo, not resulting in -1 being accepted as the answer
            $sumDiff = abs($target - $sum);

            // finding such $sum that is the least in difference with $target (finding min by sum diff)
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
