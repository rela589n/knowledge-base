See [problem](https://leetcode.com/problems/sliding-window-maximum/)

### Heap Solution

Initial thoughts is that we can use [[Max Heap]] that will store all values, in their order. Every time we need to find out the max value, we get the top of the heap, and if it is in current range, then it's the result. If not - skip it until finding the needed value.

```php
final readonly class SlidingWindowMaximumHeapSolution
{
    /**
     * @param list<int> $nums
     * @param int $windowSize
     *
     * @return list<int>
     */
    public function maxSlidingWindow(array $nums, int $windowSize): array
    {
        $maxHeap = new class extends SplMaxHeap {
            protected function compare(mixed $value1, mixed $value2): int
            {
                [$v1] = $value1;
                [$v2] = $value2;

                return $v1 <=> $v2;
            }
        };

        $results = [];

        foreach ($nums as $r => $num) {
            $maxHeap->insert([$num, $r]);

            $l = $r - $windowSize + 1;

            if ($l < 0) {
                continue;
            }

            // Extracting the maximum value for the current window from the heap.
            // If value is not in the current range, discard it.
            while (true) {
                [$maxValue, $maxValueIndex] = $maxHeap->top();

                if ($maxValueIndex >= $l) {
                    break;
                }

                $maxHeap->extract();
            }

            $results[] = $maxValue;
        }

        return $results;
    }
}
```

Thus, time complexity is [[O (N log M)]], and memory complexity is [[O (N)]].

### Monotonic Queue

Another thought is that we can use some kind of [[Monotonic data structure]] ([[Dequeue]]), where the greatest values will be inserted.

Initial thoughts were that if value is greater, then push it back. 

```
items: [5, 4, 3], 2, 1 (result: 5)
queue: [5], [4, 5], [3, 4, 5]
```

When inserting new item, we do not care about the rest smaller items. 

We don't need them, since this new bigger item will be taken in favor of the rest items.

Thus, these items won't participate in equation any longer, we may drop them.

Insertion algorithm:

```php
while (!$queue->isEmpty()) {
    [$bottomItem] = $queue->bottom();

    if ($num < $bottomItem) {
        break;
    }

    $queue->shift();
}

$queue->unshift([$num, $r]);
```

If item is smaller than existing in the queue, it should be kept.
Possibly it could become one the greatest items in the next iterations, when current max is discarded.

Therefore, when inserting it's necessary to shift all items, that are less than or equal to the given, and then insert it.

Iteration 1:
```
items: [1, 3, -1], -3, 5, 3, 6, 7
queue: [1], [3], [-1, 3]
```

Iteration 2:
```
items: 1, [3, -1, -3], 5, 3, 6, 7
queue: [-1, 3], [-3, -1, 3]
```

Iteration 3:
```
items: 1, 3, [-1, -3, 5], 3, 6, 7
queue: [-3, -1], [5]
```

Iteration 4:
```
items: 1, 3, -1, [-3, 5, 3], 6, 7
queue: [5], [3, 5]
```

Iteration 5:
```
items: 1, 3, -1, -3, [5, 3, 6], 7
queue: [3, 5], [6]
```

Iteration 6:
```
items: 1, 3, -1, -3, 5, [3, 6, 7]  
queue: [6], [7]
```

On every iteration we check if the queue's last item is it's still in range. If it's not - delete it. This way, we keep queue from using outdated items from previous iterations:

```php
while (true) {
    [$topItem, $topIndex] = $queue->top();

    if ($topIndex >= $l) {
        break;
    }

    $queue->pop();
}

// $topItem is the current max
```

Therefore, complete solution looks like this:

```php
public function maxSlidingWindow(array $nums, int $windowSize): array
{
    $queue = new SplDoublyLinkedList();

    $results = [];

    foreach ($nums as $r => $num) {
        while (!$queue->isEmpty()) {
            [$bottomItem] = $queue->bottom();

            if ($num < $bottomItem) {
                break;
            }

            $queue->shift();
        }

        $queue->unshift([$num, $r]);

        $l = $r - $windowSize + 1;

        if ($l < 0) {
            continue;
        }

        while (true) {
            [$topItem, $topIndex] = $queue->top();

            if ($topIndex >= $l) {
                break;
            }

            $queue->pop();
        }

        $results[] = $topItem;
    }

    return $results;
}
```

Time Complexity: [[O (N)]], Memory: [[O (N)]]
