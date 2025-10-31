To **capture [[Causality|Causally Dependent]] and [[Concurrent operations|Concurrent]] writes**:
- on a single node, [[Version Numbers]] are used;
- on multiple replicas, [[Version Vectors]] are used.

Client is in charge of **[[Merging concurrently written values|merging detected concurrent writes]].