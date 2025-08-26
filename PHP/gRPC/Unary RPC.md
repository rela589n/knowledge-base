---
docs:
  - https://grpc.io/docs/what-is-grpc/core-concepts/#unary-rpc
  - https://grpc.io/docs/languages/php/basics/#simple-rpc
aliases:
  - Simple RPC
---
Single request - single response:

```protobuf
rpc SayHello(HelloRequest) returns (HelloResponse);
```