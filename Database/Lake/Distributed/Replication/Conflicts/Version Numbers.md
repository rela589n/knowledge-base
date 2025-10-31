---
aliases:
  - Version
---
Algorithm ***captures* [[Causality|Dependent]] and [[Concurrent operations|Concurrent]] writes**:
- when **value** *is **written***,  **number** *is **incremented***;
- during the read, all **not overwritten versions of data are returned** to the client;
- during the write, the **version used to read the data is sent**. Client is responsible for **[[Merging concurrently written values|merging the values]] returned by read** (different due to concurrency versions of data);
- when server receives write, it **overwrites** all values with **version less than or eq to the current one** (sent along with the write), but **keeps greater versions**, because they are concurrent to the current write.
