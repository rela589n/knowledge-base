See [two sum problem](https://leetcode.com/problems/two-sum/description/) , [editorial](https://www.geeksforgeeks.org/check-if-pair-with-given-sum-exists-in-array/)

##### Brute-force

[[Brute Force]], same as in [[Two Sum (Pair Sum) In sorted Array#^b869fb]]

##### Sorting and Binary Search

We can [[Sorting|Sort]], and then apply [[Binary Search]] (same way as in [[Two Sum (Pair Sum) In sorted Array#^f25a50]]), - this is [[O (N log N)]].

##### Sorting and Two Pointers

We could [[Sorting|Sort]] and then apply [[Two pointers]] technique the same alike way as in [[Two Sum (Pair Sum) In sorted Array#^b7d57e]]. This is [[O (N log N)]].

##### Hash Map
^09cf47

We flip the array (e.g. build [[Hash Map]]) in [[O (N)]], and then traverse it once again so that for every `arr[i]` we check if it's complement `target - arr[i]` exists in the [[Hash Map]] (plus it must not be the same item). It is [[O (N)]] time and [[O (N)]] space.

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
