To **capture [[Happens-before relationship|dependent]] and [[Concurrent operations|concurrent]] writes**:
- on a single node, [[Version numbers]] are used;
- on multiple replicas, [[Version vectors]] are used.

Client is in charge of **[[Merging concurrently written values|merging detected concurrent writes]].