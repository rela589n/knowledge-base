---
aliases:
  - Minimum size SubArray Sum with negative numbers
---
See [problem](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/description/)

See [[Minimum size SubArray Sum|Shortest Subarray with sum at Least K (only positive numbers)]] for the solution that uses [[Variable-size Sliding Window]].

The key point why it doesn't work for negative numbers is because it shifts left pointer only until target stops being reached:

```php
while ($sum >= $target) {
    $length = $r - $l + 1;

    if ($length < $minLength) {
        $minLength = $length;
    }

    $sum -= $nums[$l++];
}
```

Basically, it means that if we've already shifted left pointer so that target is not reached, shifting it one more time will not make it reach. Well, it was true for positive numbers, but it isn't true for negative.

In case of negative numbers, optimal pointer shift is defined by the least sum shift. Consider this example: `[3, -1, -1, 2, 1]`, and `target=3`. It can be reached as `[3, -1, -1, 2]`, but more optimal is `[2, 1]`.

Finding optimal pointer shift could've been solved in [[O (N)]], resulting in total complexity of [[O (N**2)]], because it's also done in the loop:

```php
$shift = 0;
$leastShift = PHP_INT_MAX;
$leastShiftIndex = $this->l;

for ($i = $this->l; $i <= $this->r; ++$i) {
	$shift += $this->nums[$i];

	if ($shift < $leastShift) {
		$leastShift = $shift;
		$leastShiftIndex = $i;
	}
}

$shiftIndex = $leastShiftIndex;
```

But using [[O (log N)]] and [[O (N log N)]] is much better. It can be done with [[Min Heap]], that keeps least prefix sum at the top.

```php
private function shiftLeftPointer(): void
{
    $shiftIndex = $this->extractShiftIndex();

    $sumShift = 0;

    while ($this->l <= $shiftIndex) {
        $sumShift += $this->nums[$this->l++];
    }

    $this->sumPrefixHeap->addShift($sumShift);

    $this->sum -= $sumShift;
}
```

Thus, we just extract shift index from the heap, and shift left pointer.

Since heap contains sum, and sum is decreased, this means that the next time sum is inserted it will not correlate to the existing values. Therefore, adding this sum shift to the heap is important.

The final solution is following:

```php
final class ShortestSubarraySum
{
    /** @var list<int> */
    private array $nums;

    /** @var non-negative-int */
    private int $l;

    /** @var non-negative-int */
    private int $r;

    private int $sum;

    /**
     * Heap that contains weights of each prefix sum. The lower is the value, the lower is the weight.
     *
     * Lowest values come first (those that have the least impact).
     */
    private SplMinHeap $sumPrefixHeap;

    private int $minLength;

    /** @param list<int> $nums */
    public function shortestSubarray(array $nums, int $target): int
    {
        if ($target <= 0) {
            return 0;
        }

        $this->nums = $nums;
        $this->l = 0;
        $this->sum = 0;
        $this->sumPrefixHeap = self::newHeap();
        $this->minLength = PHP_INT_MAX;

        foreach ($this->nums as $this->r => $num) {
            $this->addUp($num);

            // if sum becomes negative, no point in keeping it (reset it)
            if ($this->sum <= 0) {
                $this->resetSum();

                continue;
            }

            // while sum is greater than the target,
            // we would want to get rid of the least significant prefix (possibly one that has negative values)
            while ($this->sum >= $target) {
                $this->checkLength();

                $this->shiftLeftPointer();
            }
        }

        if ($this->minLength === PHP_INT_MAX) {
            return -1;
        }

        return $this->minLength;
    }

    private static function newHeap(): SplMinHeap
    {
        return new class extends SplMinHeap {
            private int $shift = 0;

            public function addShift(int $shift): void
            {
                $this->shift += $shift;
            }

            public function insert($value): void
            {
                if (0 !== $this->shift) {
                    $value = ShortestSubarraySum::pair($value->prefixSum + $this->shift, $value->index);
                }

                parent::insert($value);
            }

            protected function compare(mixed $value1, mixed $value2): int
            {
                $v1 = $value1->prefixSum;
                $v2 = $value2->prefixSum;

                return parent::compare($v1, $v2);
            }
        };
    }

    private function addUp(int $num): void
    {
        $this->sum += $num;
        $this->sumPrefixHeap->insert(self::pair($this->sum, $this->r));
    }

    public static function pair(int $prefixSum, int $index): object
    {
        return new class($prefixSum, $index) {
            public function __construct(
                public int $prefixSum,
                public int $index,
            ) {
            }
        };
    }

    /** Resetting sum for the next iteration */
    private function resetSum(): void
    {
        $this->sum = 0;
        $this->l = $this->r + 1; // next iteration
        $this->sumPrefixHeap = self::newHeap();
    }

    private function checkLength(): void
    {
        if (($length = $this->length()) < $this->minLength) {
            $this->minLength = $length;
        }
    }

    private function length(): int
    {
        // +1, since both l and r are inclusive

        return $this->r - $this->l + 1;
    }

    /**
     * Decreasing sum iteratively one by one does not take into account the fact that there might
     * be some negative numbers further down the list that will increase the sum (and therefore we'd not want to break)
     * so that the sum first will become less than target, but later it would've been compensated.
     *
     * Therefore, we subtract optimal prefix by using the heap to know what is the prefix of the least impact.
     */
    private function shiftLeftPointer(): void
    {
        $shiftIndex = $this->extractShiftIndex();

        $sumShift = 0;

        while ($this->l <= $shiftIndex) {
            $sumShift += $this->nums[$this->l++];
        }

        $this->sumPrefixHeap->addShift($sumShift);

        $this->sum -= $sumShift;
    }

    private function extractShiftIndex(): int
    {
        do {
            $cutItem = $this->sumPrefixHeap->extract();
            // skip values that should've been removed already
        } while ($cutItem->index < $this->l);

        return $cutItem->index;
    }
}
```

