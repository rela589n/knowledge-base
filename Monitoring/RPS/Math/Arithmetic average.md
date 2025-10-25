---
aliases:
  - Arithmetic Mean
  - Mean
---
**Arithmetic average** is not usually used for the calculations, 
since 4 requests of 50ms and one request of 800ms 
result in 200ms average, 
while [[Median percentile]] would be 50ms, meaning that at least 50% of requests have been completed within 50ms, while this one request of 800ms was a load spike and it is not taken into account for the base case.
