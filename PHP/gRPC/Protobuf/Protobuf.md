---
aliases:
  - Protocol Buffers
  - .proto
---
*Protocol Buffers* - [[Binary data formats|binary data format]], developed by Google.

[[Protobuf|Protocol Buffers]] is similar to [[Thrift CompactProtocol]], but uses bits packing slightly different. The final payload size may differ by multiple bytes (both up and down) compared to [[Thrift CompactProtocol]].

The [[Protobuf|Protocol Buffers]] has a great approach for storing list values (`repeated` modifier). It allows to change data type of any optional field to a `repeated` representation without compatibility breaks - old code will read data as single value (take the last if multiple), while the new code will read it as list with one element.

> Whether field is required or optional doesn't affect how data is encoded. The only purpose of it is subsequent validation.
