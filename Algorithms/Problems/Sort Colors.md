See [problem](https://leetcode.com/problems/sort-colors/description/?envType=daily-question&envId=2025-05-17)

Solution uses [[Counting sort]]. It counts all values, and then fills the array with repeated values:
 
```php
function sortColors(&$nums) {
    $counts = array_count_values($nums);
    // [0 => 3, 2 => 1, 1 => 23]

    ksort($counts);

    // [0 => 3, 1 => 23, 2 => 1]

    $nums = array_merge(...array_map(fn($flag, $times) => array_fill(0, $times, $flag), array_keys($counts), $counts));
}
```