---
aliases:
  - CompactProtocol
---

The **CompactProtocol** is successor of [[Thrift BinaryProtocol]] and semantically it is the same, however it requires less space for the same data to be encoded.

It achieves this by:
- packing *[[Field tag|field tag]]* and *type* into a single byte;
- using [[Variable-length integers]].
