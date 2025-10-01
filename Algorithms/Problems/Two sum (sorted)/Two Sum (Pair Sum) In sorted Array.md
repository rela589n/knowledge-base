See [editorial](https://www.geeksforgeeks.org/pair-with-given-sum-in-sorted-array-two-sum-ii/) 

Given target number `S`, and an array `A`. Find if it's possible to get the needed sum `S` by adding any of two numbers of `A`.
##### Brute-force
^b869fb

Simple [[Brute Force]] solution is [[O (N**2)]] - traverse array two times, find all possible pairs, and check if any of them add up to `S`.
##### Binary Search
^f25a50

We can use [[Binary Search]] so that we'll get [[O (N log N)]] - traverse an array, and on every iteration it run binary search to check for the second number that will make up the desired sum (check if the complement number = `S - arr[i]` exists).
##### Hash Map

We could use [[Hash Map]] the same alike way as in [[Two Sum (Pair Sum) In unsorted Array#^09cf47]], resulting in [[O (N)]] solution.

Solution for unsorted array [[Two Sum (Pair Sum) In unsorted Array#^09cf47]]

##### Two Pointers 
^b7d57e

We could use [[Two pointers]] so that we get [[O (N)]].

1. Have pointer `L` set to the beginning of the array, pointer `R` at the end of the array. 
2. Check the sum. 
3. If it's less then the needed sum, we'd need to increase it. There's just no other way of increasing it, but by shifting the left pointer. Shifting the right won't do any good, since it only decreases the value. Thus, we **increase** the **sum** by doing **`L++`**.
4. On the other hand, if the sum is greater than the needed sum, we need to decrease it. It's just nothing else to do, but to shift the right pointer so that the sum will become smaller. Shifting the left won't help us, since it only increases the value, as the array is sorted. Thus, we **decrease** the **sum** by doing **`R--`**.

![[Two sum.png]]

[[Two pointers]] solution for [two sum](https://leetcode.com/problems/two-sum/) (unsorted, then sorted):

```php
function twoSum(array $nums, int $desiredSum) {
    $keysMap = array_keys($nums);

    array_multisort($nums, $keysMap);

    $i = 0;
    $j = count($nums) - 1;

    while ($i < $j) {
        $sum = $nums[$i] + $nums[$j];

        // [2,7,11,15]
        // [2, 15] => 17 (if sum is less than target, then we need to increase the sum,
        // therefore shifting l -> [7, 15] => 22)
        // [2, 15] => 17 (if sum is greater than target, then we need to decrease the sum,
        // to match the target, therefore shifting r -> [2, 11] => 13)

        if ($sum < $desiredSum) {
            ++$i; // increase the sum (next value of i is greater)
        } elseif ($sum > $desiredSum) {
            --$j; // decrease the sum (previous value of j is smaller)
        } else {
            return [$keysMap[$i], $keysMap[$j]];
        }
    }

	// if answer was not found
    return [];
}
```
