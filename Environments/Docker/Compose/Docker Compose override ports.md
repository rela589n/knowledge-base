To fully override the configuration part, use `!override` syntax:

`docker-compose.override.yml`:

```yaml
    minio:
        ports: !override
            - '9080:9000'
            - '9002:9001'
```