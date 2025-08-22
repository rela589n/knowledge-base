[[RoadRunner]] [[gRPC]] plugin allows you to implement a [[gRPC server]].

```shell
composer req spiral/roadrunner-grpc
```

Configuration:

```yaml
grpc:
    listen: "tcp://0.0.0.0:50051"
    tls: # Enable TLS for gRPC by providing a certificate and private key.
        cert: /etc/ssl/grpc/server/certificate.crt
        key: /etc/ssl/grpc/server/privateKey.key
        client_auth_type: require_and_verify_client_cert # full mTLS
        root_ca: /etc/ssl/grpc/client/certificate.crt # trust client certificate
    proto:
        - "src/Support/Contracts/playground/hello_world/v1/hello_world.proto"
```