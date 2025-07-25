```shell
until (/usr/bin/mc config host add myminio $${ENDPOINT} $${MINIO_ROOT_USER} $${MINIO_ROOT_PASSWORD}) do echo '...waiting...' && sleep 1; done;
```
