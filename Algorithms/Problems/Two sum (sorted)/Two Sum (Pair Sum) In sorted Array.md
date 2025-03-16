See [editorial](https://www.geeksforgeeks.org/pair-with-given-sum-in-sorted-array-two-sum-ii/) 

Given target number `S`, and an array `A`. Find if it's possible to get the needed sum `S` by adding any of two numbers of `A`.
##### Brute-force
^b869fb

Simple [[Brute Force]] solution is [[O (N**2)]] - traverse array two times, find all possible pairs, and check if any of them add up to `S`.
##### Binary Search
^f25a50

We could use [[Binary Search]] so that we get [[O (N log N)]] - traverse an array, and inside of it run binary search to check for the second number that will make up the desired sum (check if the complement number = `S - arr[i]` exists).
##### Hash Map

We could use [[Hash Map]] the same alike way as in [[Two Sum (Pair Sum) In unsorted Array#^09cf47]], resulting in [[O (N)]] solution.

Solution for unsorted array [two sum problem](https://leetcode.com/problems/two-sum/description/):

```php
function twoSum($nums, $desiredSum) {
    $map = array_flip($nums);

    foreach ($nums as $i => $num1) {
        $complement = $desiredSum - $num1;

        $j = $map[$complement] ?? -1;

        if (~$j && $j !== $i) {
            return [$i, $j];
        }
    }

    return [];
}
```
##### Two Pointers 
^b7d57e

We could use [[Two pointers]] so that we get [[O (N)]].

1. Have pointer L  as the beginning of the array, pointer R as the end of the array. 
2. Check the sum. 
3. If it's less then the needed sum, there's just no other way of increasing it, but to shift the left pointer. (shifting the right pointer won't help us, since it will decrease the value)
4. On the other hand, if the sum is greater than the needed sum, we could do nothing else, but to shift the right pointer so that it becomes smaller (shifting the left pointer won't help us, since it only increases the value, as we have the sorted array).

![[Two sum.png]]

[[Two pointers]] solution for [two sum](https://leetcode.com/problems/two-sum/) (unsorted, but sorted):

```php
function twoSum(array $nums, int $desiredSum) {
    $keysMap = array_keys($nums);

    array_multisort($nums, $keysMap);

    $i = 0;
    $j = count($nums) - 1;

    while ($i < $j) {
        $sum = $nums[$i] + $nums[$j];

        // [2,7,11,15]
        // [2, 15] => 17 (if sum is less than target, then we need to increase sum,
        // therefore shifting l -> [7, 15] => 22)
        // [2, 15] => 17 (if sum is greater than target, then we need to decrease sum,
        // to match the target, therefore shifting r -> [2, 11] => 13)

        if ($sum < $desiredSum) {
            ++$i; // increase sum
        } elseif ($sum > $desiredSum) {
            --$j; // decrease sum
        } else {
            return [$keysMap[$i], $keysMap[$j]];
        }
    }

	// if answer was not found
    return [];
}
```
