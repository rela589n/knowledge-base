See [problem](https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=leetcode-75), [diagram](https://docs.google.com/spreadsheets/d/1iViE45t-sob6Kb6e2rX8acUH5_4fvbHQRCKEo9H7xto/edit?usp=sharing)

Components:
- [[Sub-Region]]

![[Container with most water.png]]

If the height of the next position is the same (or lower) as the current, there's no point in moving to that position, since it would only decrease the amount of water (we need to increase).

For example, moving from 1 to 2 would decrease the amount.

If the height of the next position is higher than the current, it might (or might not) increase the amount of water (it depends):

- if the opposite position is less than or equal to the current, switch of the current position would only decrease amount of water. For example, switch from 5 to 4 would decrease.

- if the opposite position is greater than the current, change of the current position to the greater one, might increase the value.

Therefore, if we iterate through the whole range and will always change the smaller of two pointers, we'd eventually traverse all possible increases of the value.

The solution uses [[Two pointers]] approach, and every time smaller pointer is shifted so that it might eventually result in higher amount.

```php
function maxArea($heights) {

    $l = 0;
    $r = count($heights) - 1;

    $maxArea = 0;

    while ($l < $r) {
        $area = ($r - $l) * min($heights[$l], $heights[$r]);

        $maxArea = max($area, $maxArea);

        if ($heights[$l] < $heights[$r]) {
            ++$l;
        } else {
            --$r;
        }
    }

    return $maxArea;
}
```