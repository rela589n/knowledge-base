---
aliases:
  - Monotonic Queue
  - Monotonic Stack
---
Queue, where values are monotonically inserted. So, if we insert new value, we drop all the values, that violate the monotony of the queue. These items are not needed in solving the problem anyway.

When new value is inserted, usually some values that are less than the given are dropped if favor of it.
