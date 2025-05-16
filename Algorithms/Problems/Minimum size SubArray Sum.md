---
aliases:
  - Shortest Subarray with sum at Least K (only positive numbers)
---
See [problem](https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=problem-list-v2&envId=sliding-window).

## Sliding Window

Components:
- [[Sliding Range]]

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

	// At this point, we accumulate that $sum until it reaches the $target
	foreach ($nums as $r => $num) {
		$sum += $num;

	    // Once current sum becomes greater than target, we start descreasing the size of subarray by shifting the left pointer - 
	    // this allows us to find the array of minimal length that has sum greater than or equal to target
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

> Note that this solution doesn't handle negative numbers.

For the solution that handles negative numbers as well, it's necessary to use more complex logic to determine left pointer shift. See [[Shortest Subarray with sum at Least K|Minimum size SubArray Sum with negative numbers]].

## Binary Search and [[Fixed-size Sliding Window]]

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
