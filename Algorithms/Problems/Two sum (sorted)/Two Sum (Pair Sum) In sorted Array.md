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
##### Two Pointers 
^b7d57e

We could use [[Two pointers]] so that we get [[O (N)]].

1. Have pointer L  as the beginning of the array, pointer R as the end of the array. 
2. Check the sum. 
3. If it's less then the needed sum, there's just no other way of increasing it, but to shift the left pointer. (shifting the right pointer won't help us, since it will decrease the value)
4. On the other hand, if the sum is greater than the needed sum, we could do nothing else, but to shift the right pointer so that it becomes smaller (shifting the left pointer won't help us, since it only increases the value, as we have the sorted array).

![[Two sum.png]]