To fully override the configuration part, use `!override` syntax:

```
    minio:
        ports: !override
            - '9080:9000'
            - '9002:9001'
```