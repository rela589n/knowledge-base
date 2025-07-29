---
aliases:
  - Monotonic Queue
  - Monotonic Stack
---
Queue, in which the values are monotonically inserted. So, if we insert a new value, we drop all the values that violate the monotonic property of the queue (`[1,4,5]` - to insert `3` we either drop 4 and 5 (`[1,3]`) or drop 1 (`[3,4,5]`)). Dropped items are not needed in solving the problem anyway.

When new value is inserted, usually some values that are less than the given are dropped if favor of it.
