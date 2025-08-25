---
docs:
  - https://grpc.io/docs/what-is-grpc/core-concepts/#unary-rpc
---
Single request - single response:

```protobuf
rpc SayHello(HelloRequest) returns (HelloResponse);
```