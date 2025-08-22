You'd need to:
- install [[gRPC extension]] and [[gRPC composer package|gRPC package]];
- install [[Protobuf extension]];
- install [[Buf]];
- define [[Protobuf|.proto]] file;
- [[Buf code generation|generate]] php classes with Buf;
- configure [[RoadRunner gRPC plugin]];
- implement the service;
- use [[Baldinof RoadRunner Bundle]] to start worker;
- write test using the client.
