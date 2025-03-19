See [problem](https://leetcode.com/problems/add-two-numbers/).

The algorithm uses [[Recursion]] to traverse the [[Linked list]] and sum the numbers.

```php
/**
 * Definition for a singly-linked list.
 * class ListNode {
 *     public $val = 0;
 *     public $next = null;
 *     function __construct($val = 0, $next = null) {
 *         $this->val = $val;
 *         $this->next = $next;
 *     }
 * }
 */
class Solution {

    /**
     * @param ListNode $l1
     * @param ListNode $l2
     * @return ListNode
     */
    function addTwoNumbers($l1, $l2) {
        return $this->doAdd($l1, $l2, 0);
    }

    function doAdd($l1, $l2, $extra) {
        if (null === $l1 && null === $l2 && 0 === $extra) {
            return null;
        }

        $d1 = $l1?->val ?? 0;
        $d2 = $l2?->val ?? 0;

        $sum = $d1 + $d2 + $extra;

        $resultDigit = $sum % 10;

        $next = $this->doAdd($l1?->next, $l2?->next, intdiv($sum, 10));

        return new ListNode($resultDigit, $next);
    }
}
```