[[Buf]] managed mode allows to specify *language-specific* configurations in `buf.gen.yaml` instead of [[Protobuf|.proto]]-files.

```yaml
managed:
  enabled: true
  override:
    - file_option: php_namespace
      value: Weather\Grpc
  # use this to disable reset
  disable:
    - file_option: php_namespace # don't reset it to the default
    - file_option: php_metadata_namespace
```


