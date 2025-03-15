See [editorial](https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/)
##### Brute-force

We could traverse all possible triplets in the array to find out if there are any that add up to `S`. This is [[O (N ** 3)]]

##### Hash Map

First of all, we build [[Hash Map]] of the initial array (keys are values, and values are keys).

Then, we traverse an array with two inner loops and check if `complement_part = S - arr[i] - arr[j]` exists in the hash map. If it does, then we've found the answer. (also, it's necessary to check that the complement part is neither `i` nor `j` item, as we can't use same item twice or thrice).

This solution uses [[O (N**2)]] time and [[O (N)]] space.

##### Two-sum

First of all, we [[Sorting|Sort]] the array. Then, we iterate in the outer loop over values, and for each `arr[i]` we run [[Two Sum (Pair Sum) In sorted Array#^b7d57e]] two pointers solution. Therefore, it's [[O (N**2)]].

Example from [leetcode](https://leetcode.com/problems/3sum) - need to write all (unique) solutions that produce sum of 0:

```php
function threeSum(array $nums) {
    sort($nums);

    $solutions = [];

    for ($i = 0, $n = count($nums); $i < $n - 2; ++$i) {
        $first = $nums[$i];
        $j = $i + 1;
        $k = $n - 1;

        // Two pointers solution [j ->> .... <-- k]
        // J moves right, K moves left

        while ($j < $k) {
            $second = $nums[$j];
            $third = $nums[$k];

            $sum = $first + $second + $third;

            if ($sum < 0) {
                ++$j;
            } elseif ($sum > 0) {
                --$k;
            } else {
                $solutions[] = [$first, $second, $third];

                // We need to find another solution, and it should be different from this one
                // Therefore, moving right pointer lefter until $nums[$k] is different from current value.
                do {
                    --$k;
                } while ($third === $nums[$k]);
            }
        }

        // [-4,-1,-1,0,1,2]
        //   i  j        k
        //   i     j     k
        //   i       j   k
        //   i         j k
        //
        // [-4,-1,-1,0,1,2]
        //      i  j     k - solution (-1, -1, 2)
        //      i  j   k   - moving j, since it's -1
        //      i    j k   - solution (-1, 0, 1)

        // Deduplicate Solutions
        // (using the same value for $first won't produce any
        //  different result from the one already produced)
        while ($first === $nums[$i + 1]) {
            ++$i;
        }
    }

    return $solutions;
}
```