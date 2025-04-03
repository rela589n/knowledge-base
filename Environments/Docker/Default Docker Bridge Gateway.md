---
aliases:
  - 172.17.0.1
  - host.docker.internal
  - host-gateway
---
Host IP (your local machine, on which docker runs) is 172.17.0.1.

Yet, it is recommended to use `host.docker.internal:host-gateway` instead, to work for MacOS and Windows.

Container hosts configuration:
```yaml
container:
    image: your-image:v1.1
    environment:
        - "PHP_IDE_CONFIG=serverName=file.loc"
    extra_hosts:
        - "host.docker.internal:host-gateway"
        - "file.loc:host-gateway"
```

In this example, you could contact host machine by `host.docker.internal`.
