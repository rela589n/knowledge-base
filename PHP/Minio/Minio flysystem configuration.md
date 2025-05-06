```yaml
parameters:
    env(BAKING_STORE_FS_REGION): '%env(MINIO_FS_REGION)%'
    env(BAKING_STORE_FS_ENDPOINT): '%env(MINIO_FS_ENDPOINT)%'
    env(BAKING_STORE_FS_VERSION): '%env(MINIO_FS_VERSION)%'
    env(BAKING_STORE_FS_KEY): '%env(MINIO_FS_KEY)%'
    env(BAKING_STORE_FS_SECRET): '%env(MINIO_FS_SECRET)%'

flysystem:
    storages:
        app_baking_store.file_storage:
            adapter: aws
            options:
                client: app_baking_store.flysystem.client
                bucket: baking_store
                streamReads: true

services:
    _defaults:
        autowire: true
        autoconfigure: true

    app_baking_store.flysystem.client:
        class: Aws\S3\S3Client
        arguments:
            -   region: '%env(BAKING_STORE_FS_REGION)%'
                endpoint: '%env(BAKING_STORE_FS_ENDPOINT)%'
                version: '%env(BAKING_STORE_FS_VERSION)%'
                use_path_style_endpoint: true
                credentials:
                    key: '%env(BAKING_STORE_FS_KEY)%'
                    secret: '%env(BAKING_STORE_FS_SECRET)%'

```