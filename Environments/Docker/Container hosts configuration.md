---
aliases:
  - host.docker.internal
---

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
