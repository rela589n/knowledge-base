[[Buf]] managed mode allows to specify language-specific configurations in `buf.gen.yaml` instead of [[Protobuf|proto]]-files.

```yaml
managed:
  enabled: true
  override:
    - file_option: php_namespace
      value: Weather\Grpc
```
