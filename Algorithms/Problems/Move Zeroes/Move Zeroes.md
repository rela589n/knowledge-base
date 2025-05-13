See [problem](https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75).

Naive solution is to use additional memory, filter the original array, count zeros, and reassign the array with that filtered array plus zeros array:

```php
function moveZeroes(&$nums) {
    $numsNoZero = array_values(array_filter($nums));
    $zeroCount = count($nums) - count($numsNoZero);

    $nums = [...$numsNoZero, ...array_fill(0, $zeroCount, 0)];
}
```

This is fast approach, that uses [[O (N)]] time, and [[O (N)]] memory.

### [[Insertion Sort]]-based Solution

Another solution would be to use [[Insertion Sort]]-based approach, moving every non-zero item to the beginning. 
It seems to take [[O (N**2)]] time (almost 2 seconds on leetcode).

```php
function moveZeroes(&$nums) {
    // 0 0 1 0 2 3
    // 1 2 0 3 0 0

    for ($i = 1; $i < count($nums); ++$i) {
        if ($nums[$i] === 0) {
            continue;
        }

        for ($j = $i - 1; $j >= 0 && $nums[$j] === 0; --$j) {
            $nums[$j] = $nums[$j + 1];
            $nums[$j + 1] = 0;
        }
    }
}
```

### [[Two pointers]]-based Solution

Keep track of zero-space start offset. If we meet any non-zero value, put it at the place of the first zero item:

```php
function moveZeroes(&$nums) {
    // z   i
    // 0 0 1 0 2 3

    //   z   i
    // 1 0 0 0 2 3

    //   z     i
    // 1 0 0 0 2 3

    //     z     i
    // 1 2 0 0 0 3

	// Offset to the first zero-value (if there's one)
	$zeroOffset = 0;
	
	foreach($nums as $i => $num) {
	    if ($num !== 0) {
	        $nums[$i] = 0;
	        $nums[$zeroOffset++] = $num;
	    }
	}
}
```

This is different from previous one, since we don't have to move through all this gap of zero-space just to put value in front. On the other side, we put the value right by the index that we keep track of.