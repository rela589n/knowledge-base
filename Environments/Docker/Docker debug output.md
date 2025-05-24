---
aliases:
  - Docker build debug
---
If you run build as flag:
```shell
docker compose up -d --build
```

Then, in docker file you should dump content and exit:

```shell
RUN echo $(pwd) && exit 1
```

If it's necessary to keep going, consider using `progress=plain`

```shell
docker compose build --progress=plain
```
