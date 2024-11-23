```yaml
    centrifugo:
        image: centrifugo/centrifugo:v5.1.1
        command: centrifugo --config=/centrifugo/config.json
        volumes:
            - "./docker-configs/centrifugo_config.json:/centrifugo/config.json"
            - "./Resources/prototype:/centrifugo/prototype"
        ports:
            - "127.0.0.1:8008:8000"
            - "127.0.0.1:3003:3000"
```

The `prototype` folder contains index.html file: [[Centrifugo hello world client]].