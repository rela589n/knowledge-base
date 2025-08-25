---
docs:
  - https://grpc.io/docs/what-is-grpc/core-concepts/#client-streaming-rpc
---
Client sends a streamed Request, server returns a Reponse.

```protobuf
rpc LotsOfGreetings(stream HelloRequest) returns (HelloResponse);
```