See [problem](https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=problem-list-v2&envId=sliding-window).

## Sliding Window

Complexity: [[O (N)]]

This could be solved with [[Variable-size Sliding Window]] :

```php
function minSubArrayLen($target, $nums) {
    $n = count($nums);

    // [2,3,1,2,4,3]        
    // we keep increasing the window until we reach target, 
    // then we decrease the window until we stop reaching the target

	$l = 0;
	$sum = 0;
	$minLength = PHP_INT_MAX;

	foreach ($nums as $r => $num) {
		$sum += $num;

		while ($sum >= $target) {
			$length = $r - $l + 1;

			if ($length < $minLength) {
				$minLength = $length;
			}

			$sum -= $nums[$l++];
		}
	}

	if ($minLength === PHP_INT_MAX) {
		return 0;
	}

	return $minLength;
}
```

> Note that this solution doesn't handle negative numbers well.

Another solution, more robust is this:

```php
// At this point, we assume that $currentSum < $target, and maintain this state in the loop
while ($r < $n) {
    $currentSum += $nums[$r++];

    // Once current sum becomes greater than target, we start descreasing the size of subarray by shifting left pointer - 
    // this allows us to find the array of minimal length that has sum greater than or equal to target
    while ($currentSum >= $target && $l < $r) {
        $length = $r - $l;

        if ($length < $minimalLength) {
            $minimalLength = $length;
        }

        $currentSum -= $nums[$l];

        ++$l;
    }
}
```

This is likely to handle negative numbers as well.

## Binary Search and Sliding Window 

Complexity: [[O (N log N)]]

This also could be solved using [[Binary Search]] (over array length) and [[Fixed-size Sliding Window]] approach:

```php
function minSubArrayLen($target, $nums)
{   
    $n = count($nums);

    $l = 1;
    $r = $n;

    $minLen = 0;

    while ($l <= $r) {
        $m = $l + (($r - $l) >> 1);

        if ($this->getWindowMaxSum($m, $nums) >= $target) {
            $minLen = $m;

            $r = $m - 1;
        } else {
            $l = $m + 1;
        }
    }

    return $minLen;
}
```

The second `getWindowMaxSum()` function is [[Window Max Sum]].
