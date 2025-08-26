---
docs:
  - https://grpc.io/docs/what-is-grpc/core-concepts/#unary-rpc
---
Request results in a stream of responses. 
Client receives them all until there are no more messages.

````protobuf
rpc LotsOfReplies(HelloRequest) returns (stream HelloResponse);
```