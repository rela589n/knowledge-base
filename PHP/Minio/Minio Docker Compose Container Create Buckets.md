Use this combination of `entrypoint` and `command`.

```yaml
minio:  
    image: minio/minio:latest  
    entrypoint: sh  
    command:  
        - -c  
        - mkdir -p /data/{bucket1,bucket2,bucket3} &&  
            minio server /data --console-address ':9001'  
    environment:  
        MINIO_ROOT_USER: admin  
        MINIO_ROOT_PASSWORD: top-secret  
    volumes:  
        - minio_data:/data  
    ports:  
        - '127.0.0.1:9090:9000'  
        - '127.0.0.1:9001:9001'
```