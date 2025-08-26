---
docs:
  - https://grpc.io/docs/what-is-grpc/core-concepts/#deadlines
---
Server accepts stream, and returns stream.

```protobuf
rpc StreamingHello(stream HelloRequest) returns (stream HelloResponse);
```

The server and client can play “ping-pong” - one sends the request, and receives a response, and then sends another request based on the response.
