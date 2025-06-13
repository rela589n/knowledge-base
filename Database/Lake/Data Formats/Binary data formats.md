---
aliases:
  - binary data format
---
For internal use, when there are terabytes of data, it is really reasonable to stick with the most compact format. 

Binary protocols require schema for it's data (code generation is available).

Pure binary formats:
- [[Thrift]];
- [[Protobuf]].

The big difference to [[Binary JSON formats]] is that field names are never stored as part of data, but [[Field tag|field tags]] are used instead.