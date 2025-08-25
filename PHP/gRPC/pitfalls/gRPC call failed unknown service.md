The problem is with [[RoadRunner gRPC plugin]] configuration:

This doesn't work:
```yaml
    proto:
        - "src/Support/Contracts/{,*/}*.proto"
```

