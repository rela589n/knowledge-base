```yaml
app_contracts.grpc_channel_credentials:
    class: Grpc\ChannelCredentials
    factory: [ ~ ,'createSsl' ]
    arguments:
        - '%env(file:GRPC_SERVER_CERT_PATH)%'
        - '%env(file:GRPC_CLIENT_KEY_PATH)%'
        - '%env(file:GRPC_CLIENT_CERT_PATH)%'
```
