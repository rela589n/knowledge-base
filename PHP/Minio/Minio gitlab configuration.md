```yaml
services:
    - name: axllent/mailpit:latest
      alias: mailpit
    - name: bitnami/minio:latest
      alias: minio
variables:
    MINIO_DEFAULT_BUCKETS: bucket_name
```
